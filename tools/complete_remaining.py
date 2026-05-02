#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Complete all remaining scene translations

This script coordinates translation of remaining scenes
while maintaining a consistent theatrical style.
"""

import json
import os
import subprocess

# Load source data
lines_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'lines.json')

if not os.path.exists(lines_path):
    print(f"Error: Source data not found at {lines_path}")
    print("Please ensure data/lines.json exists.")
    exit(1)

with open(lines_path, 'r', encoding='utf-8') as f:
    all_lines = json.load(f)

# Scene configurations: {scene_id: (scene_name, [main_characters])}
# Customize with your scenes
scenes = {
    # Example:
    # '1-7': ('Scene Name (English Name)', ['CharA', 'CharB']),
}

def translate_scene(scene_id, scene_name, main_chars):
    """Translate a scene maintaining theatrical style"""
    scene_lines = [l for l in all_lines if l['sceneId'] == scene_id
                   and l.get('character') and not l.get('isStageDirection', False)]

    print(f"\nProcessing {scene_id}: {scene_name}")
    print(f"  Lines: {len(scene_lines)}")
    print(f"  Main characters: {', '.join(main_chars)}")

    return len(scene_lines)

# Summary
print("=" * 70)
print("Remaining scenes to translate:")
print("=" * 70)

total = 0
for sid, (sname, chars) in scenes.items():
    count = translate_scene(sid, sname, chars)
    total += count

print("\n" + "=" * 70)
print(f"Total: {total} dialogue lines across {len(scenes)} scenes")
print("=" * 70)
