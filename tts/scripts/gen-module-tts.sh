#!/bin/bash
# Generate TTS audio for a single subelement markdown file.
# Usage: gen-module-tts.sh <subelement.md> [voice]
set -e

MD_FILE="$1"
VOICE="${2:-will}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"

if [ -z "$MD_FILE" ]; then
    echo "Usage: $0 <subelement.md> [voice]"
    exit 1
fi

if [ ! -f "$MD_FILE" ]; then
    echo "File not found: $MD_FILE" >&2
    exit 1
fi

OUTPUT="${MD_FILE%.md}.mp3"
WORK_DIR=$(mktemp -d)

cleanup() { rm -rf "$WORK_DIR"; }
trap cleanup EXIT

echo "==> $(basename "$MD_FILE") -> $(basename "$OUTPUT")"

python3 "$SCRIPT_DIR/gen-to-tts.py" "$MD_FILE" > "$WORK_DIR/spoken.txt"

bash "$SCRIPT_DIR/generate-audio.sh" "$WORK_DIR/spoken.txt" "$OUTPUT" "$VOICE"
