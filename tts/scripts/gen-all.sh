#!/bin/bash
# Regenerate all 20 subelement MP3s (10 study guides + 10 question files).
# Usage: gen-all.sh [voice]
set -e

VOICE="${1:-will}"
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"
SUBELEMENTS_DIR="$REPO_DIR/subelements"
KOKORO="$HOME/.openclaw/skills/voice/scripts/tts-kokoro"

echo "=== General Class Study Guide — Full TTS Generation ==="
echo "Voice: $VOICE"
echo "Repo:  $REPO_DIR"
echo ""

# Verify TTS server is reachable
echo "-> Checking TTS server..."
CHECK=$(python3 "$KOKORO" --check 2>&1)
if ! echo "$CHECK" | python3 -c "import sys,json; d=json.load(sys.stdin); sys.exit(0 if d.get('available') else 1)" 2>/dev/null; then
    echo "ERROR: TTS server not reachable." >&2
    echo "$CHECK" >&2
    exit 1
fi
echo "   Server OK"
echo ""

FAILED=0
DONE=0
TOTAL=20

# Study guide files (narrative) — G0 through G9
STUDY_FILES=$(ls "$SUBELEMENTS_DIR"/*.md | grep -v "\-questions\.md" | sort)

# Question files
QUESTION_FILES=$(ls "$SUBELEMENTS_DIR"/*-questions.md | sort)

ALL_FILES="$STUDY_FILES
$QUESTION_FILES"

# Process each file
IDX=0
for md_file in $ALL_FILES; do
    IDX=$((IDX + 1))
    name=$(basename "$md_file" .md)
    echo "--- [$IDX/$TOTAL] $name ---"
    if bash "$SCRIPT_DIR/gen-module-tts.sh" "$md_file" "$VOICE"; then
        DONE=$((DONE + 1))
    else
        echo "FAILED: $name" >&2
        FAILED=$((FAILED + 1))
    fi
    echo ""
done

echo ""
echo "=== Summary: $DONE/$TOTAL complete, $FAILED failed ==="

if [ "$FAILED" -gt 0 ]; then
    exit 1
fi
