#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Translation Creation Script
Translates all dialogue from Chinese to English for subtitle generation.

This script contains a character-to-pinyin mapping and a translations
dictionary organized by scene. It loads dialogue data and creates
a complete translation mapping.
"""

import json
import os

# Character pinyin mapping
# Map each Chinese character name to its pinyin equivalent (used for subtitle display)
CHAR_PINYIN = {
    # Example entries - customize for your production:
    # '云': 'YUN',
    # '敏': 'MIN',
    # '萧': 'XIAO',
}

# Complete translations dictionary - organized by scene
# Each entry: (chinese_text, english_translation)
TRANSLATIONS = {
    # Example - Scene 1-2:
    # "1-2": [
    #     ("Chinese line 1", "English translation 1"),
    #     ("Chinese line 2", "English translation 2"),
    # ],
}

def load_all_dialogues():
    """Load all dialogues from the JSON file"""
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'dialogues_for_translation.json')
    with open(data_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data['dialogues']

def create_translation_mapping():
    """Create a complete translation mapping for all dialogues"""
    print("Loading dialogues...")
    dialogues = load_all_dialogues()

    # Create a mapping from content to translation based on our translations dict
    content_to_translation = {}
    for scene_id, translations in TRANSLATIONS.items():
        for chinese, english in translations:
            content_to_translation[chinese] = english

    print(f"Total dialogues: {len(dialogues)}")
    print(f"Pre-translated: {len(content_to_translation)}")

    # Count how many we've translated so far
    translated_count = 0
    for d in dialogues:
        if d['content'] in content_to_translation:
            translated_count += 1

    print(f"Coverage: {translated_count}/{len(dialogues)} ({100*translated_count/len(dialogues):.1f}%)")
    return dialogues, content_to_translation

if __name__ == "__main__":
    create_translation_mapping()
