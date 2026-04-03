#!/bin/bash
# Generate TTS audio from a spoken-text file.
# Usage: generate-audio.sh <input.txt> <output.mp3> [voice]
set -e

INPUT="$1"
OUTPUT="$2"
VOICE="${3:-will}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
TTS_DIR="$SCRIPT_DIR/.."
WORK_DIR=$(mktemp -d)
KOKORO="$HOME/.openclaw/skills/voice/scripts/tts-kokoro"

if [ -z "$INPUT" ] || [ -z "$OUTPUT" ]; then
    echo "Usage: $0 <input.txt> <output.mp3> [voice]"
    exit 1
fi

cleanup() { rm -rf "$WORK_DIR"; }
trap cleanup EXIT

echo "=== Technician Study Guide TTS Generator ==="
echo "Input:  $INPUT"
echo "Output: $OUTPUT"
echo "Voice:  $VOICE"

echo "-> Applying pronunciation dictionary..."
python3 "$SCRIPT_DIR/apply-pronunciation.py" "$INPUT" "$TTS_DIR/pronunciation.txt" > "$WORK_DIR/pronounced.txt"

echo "-> Chunking text..."
python3 "$SCRIPT_DIR/chunk-text.py" "$WORK_DIR/pronounced.txt" --max-chars 2000 --output-dir "$WORK_DIR" --prefix chunk

echo "-> Generating audio chunks..."
CHUNKS=("$WORK_DIR"/chunk_*.txt)
TOTAL=${#CHUNKS[@]}
IDX=0

for chunk in "${CHUNKS[@]}"; do
    IDX=$((IDX + 1))
    base=$(basename "$chunk" .txt)
    echo "  [$IDX/$TOTAL] $base..."
    RESULT=$(python3 "$KOKORO" "$(cat "$chunk")" --voice "$VOICE" --format mp3 --output "$WORK_DIR/${base}.mp3" 2>&1)
    if ! echo "$RESULT" | python3 -c "import sys,json; d=json.load(sys.stdin); sys.exit(0 if d.get('success') else 1)" 2>/dev/null; then
        echo "  ERROR on $base: $RESULT" >&2
        exit 1
    fi
done

echo "-> Concatenating ${TOTAL} chunks..."
ls "$WORK_DIR"/chunk_*.mp3 | sort | sed "s|.*|file '&'|" > "$WORK_DIR/concat.txt"
ffmpeg -y -f concat -safe 0 -i "$WORK_DIR/concat.txt" -c:a libmp3lame -b:a 128k "$OUTPUT" 2>/dev/null

DURATION=$(ffprobe -v quiet -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "$OUTPUT" 2>/dev/null || echo "?")
SIZE=$(ls -lh "$OUTPUT" | awk '{print $5}')
if [ "$DURATION" != "?" ]; then
    python3 -c "d=float('$DURATION'); m=int(d//60); s=int(d%60); print(f'=== Done: {m}m {s}s, $SIZE ===')"
else
    echo "=== Done: $SIZE ==="
fi
