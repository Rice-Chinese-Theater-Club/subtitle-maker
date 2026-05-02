#!/bin/bash
# Batch complete all remaining scenes
# Usage: ./batch_complete.sh

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_DIR"

# List your scenes here
scenes="1-2 1-3 1-4"

for scene in $scenes; do
    echo "=== Processing scene $scene ==="

    json_file="translations/scene_${scene}_translation.json"
    if [ -f "$json_file" ]; then
        python3 tools/generate_subtitles_ppt.py "$json_file"
    else
        echo "  Translation file not found: $json_file"
    fi
done

echo ""
echo "All scenes processed."
