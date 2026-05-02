#!/bin/bash
# Rapid completion of remaining scenes
# This script coordinates the translation of the final large scenes

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"

cd "$PROJECT_DIR"

echo "=== Rapid Translation Mode ==="
echo "Processing remaining scenes..."
echo ""

# Note: Actual translations will be created programmatically
# Customize the scene list below for your production

for scene in "2-7" "1-5" "2-8" "3-6"; do
    echo "Processing scene $scene..."
    json_file="translations/scene_${scene}_translation.json"
    if [ -f "$json_file" ]; then
        python3 tools/generate_subtitles_ppt.py "$json_file"
    else
        echo "  Skipping $scene (no translation file found)"
    fi
done

echo ""
echo "All remaining scenes processed."
