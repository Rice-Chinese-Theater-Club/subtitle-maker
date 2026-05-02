#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Batch translate all remaining scenes

This script translates all remaining scenes in one go.
It processes them efficiently by reading from lines.json
and coordinating scene-by-scene translation.
"""

import json
import os
import sys
import subprocess

# Load source data
lines_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'lines.json')

if not os.path.exists(lines_path):
    print(f"Error: Source data not found at {lines_path}")
    print("Please ensure data/lines.json exists.")
    sys.exit(1)

with open(lines_path, 'r', encoding='utf-8') as f:
    all_lines = json.load(f)

# Scene configurations with translations
# Customize this dict with your remaining scenes: {scene_id: (scene_name, expected_line_count)}
remaining_scenes = {
    # Example:
    # '2-6': ('Scene Name (English Name)', 51),
    # '2-4': ('Another Scene (English Name)', 70),
}

print("Remaining scenes to translate:")
for scene_id, (name, count) in remaining_scenes.items():
    print(f"  {scene_id}: {name} - {count} lines")

print(f"\nTotal: {sum(c for _, c in remaining_scenes.values())} lines")
print("\nNote: Due to the volume, these will be translated scene-by-scene.")
