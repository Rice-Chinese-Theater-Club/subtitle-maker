#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analyze translation lengths to identify problematic slides.
Reads a translation JSON and reports which lines exceed character thresholds.
"""

import json
import sys
import os


def analyze(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    translations = data['translations']

    print(f"Translation length analysis: {os.path.basename(json_path)}")
    print("=" * 80)
    print()

    # Find translations exceeding different thresholds
    thresholds = [100, 150, 200, 250]
    long_translations = {t: [] for t in thresholds}

    for item in translations:
        length = len(item['translation'])
        for threshold in thresholds:
            if length > threshold:
                long_translations[threshold].append({
                    'index': item['index'],
                    'length': length,
                    'character': item['characterPinyin'],
                    'translation': item['translation']
                })

    # Print statistics
    print(f"Total lines: {len(translations)}")
    print()

    for threshold in thresholds:
        count = len(long_translations[threshold])
        percentage = (count / len(translations)) * 100
        print(f"Lines exceeding {threshold} chars: {count} ({percentage:.1f}%)")

    print()
    print("=" * 80)
    print()

    # Show details of problematic translations (>100 chars)
    print("Lines exceeding 100 characters:")
    print()

    for item in long_translations[100]:
        print(f"#{item['index'] + 1} | {item['character']} | {item['length']} chars")
        print(f"  Original: {translations[item['index']]['original'][:50]}...")
        print(f"  Translation: {item['translation']}")
        print()
        print("-" * 80)
        print()

    # Show the longest one in detail
    longest = max(translations, key=lambda x: len(x['translation']))
    print()
    print("=" * 80)
    print("Longest line:")
    print(f"#{longest['index'] + 1} | {longest['characterPinyin']} | {len(longest['translation'])} chars")
    print()
    print(f"Original: {longest['original']}")
    print()
    print(f"Translation: {longest['translation']}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 analyze_length.py <translation_json_file>")
        sys.exit(1)
    analyze(sys.argv[1])
