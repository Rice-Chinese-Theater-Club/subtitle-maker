#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translate Scene Helper Script

Usage:
    python3 translate_scene.py <scene_id> <translations_dict>

This script:
1. Extracts dialogue from lines.json for the specified scene
2. Creates a translation JSON file with the provided translations
3. Generates a PPT from the translation JSON
"""

import json
import sys
import os

def create_translation_file(scene_id, translations_list, scene_name_en, pinyin_map):
    """
    Create a translation JSON file for a given scene

    Args:
        scene_id: Scene ID (e.g., "1-2")
        translations_list: List of English translations
        scene_name_en: English name for the scene
        pinyin_map: Dictionary mapping Chinese character names to pinyin
    """
    # Load source data
    lines_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'lines.json')
    with open(lines_path, 'r', encoding='utf-8') as f:
        lines = json.load(f)

    # Extract scene dialogue
    scene_data = [line for line in lines if line['sceneId'] == scene_id and line.get('character') and not line.get('isStageDirection', False)]

    if len(scene_data) != len(translations_list):
        print(f"Warning: Found {len(scene_data)} dialogue lines but {len(translations_list)} translations provided")

    # Get scene name from first stage direction
    scene_name_cn = ""
    for line in lines:
        if line['sceneId'] == scene_id and line.get('isStageDirection'):
            scene_name_cn = line['content']
            break

    # Create translation data
    translation_data = {
        "sceneId": scene_id,
        "sceneName": f"{scene_name_cn} ({scene_name_en})" if scene_name_en else scene_name_cn,
        "totalLines": len(scene_data),
        "translations": []
    }

    for idx, line in enumerate(scene_data):
        if idx < len(translations_list):
            translation_data["translations"].append({
                "index": idx,
                "character": line["character"],
                "characterPinyin": pinyin_map.get(line["character"], line["character"].upper()),
                "original": line["content"],
                "translation": translations_list[idx]
            })

    # Write to file
    output_path = os.path.join(os.path.dirname(__file__), '..', 'translations', f'scene_{scene_id}_translation.json')
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(translation_data, f, ensure_ascii=False, indent=2)

    print(f"Created scene_{scene_id}_translation.json")
    print(f"Translated {len(translation_data['translations'])} lines")

    return output_path

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translate_scene.py <scene_id>")
        print("Example: python3 translate_scene.py 2-2")
        sys.exit(1)

    scene_id = sys.argv[1]
    print(f"Processing scene {scene_id}...")

if __name__ == "__main__":
    main()
