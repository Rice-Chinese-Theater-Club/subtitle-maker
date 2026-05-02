#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test the text splitting function on long sentences.
Verifies that split_long_text breaks text at natural boundaries.
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'tools'))
from generate_subtitles_ppt import split_long_text

# Example test cases - customize with your own long translations
test_cases = [
    {
        'id': '#1',
        'char': 'A',
        'text': "This is a short sentence that should not be split at all."
    },
    {
        'id': '#2',
        'char': 'B',
        'text': ("After regretting you feel guilty, so you pray. "
                 "But halfway through praying you realize you don't have any faith. "
                 "But philosophical questions don't really bother you.")
    },
    {
        'id': '#3',
        'char': 'A',
        'text': ("Having drinks with a few close friends, heart-to-heart talks — "
                 "this satisfies you completely. But in the midst of this seemingly "
                 "pleasant process, sometimes you suddenly feel detached, like a cold "
                 "observer, finding it all boring and pointless, then feeling a vast "
                 "and inexplicable loneliness.")
    },
]

print("Long text splitting test")
print("=" * 80)
print()

for case in test_cases:
    print(f"{case['id']} | {case['char']} | Original length: {len(case['text'])} chars")
    print("-" * 80)

    parts = split_long_text(case['text'])

    print(f"Split into {len(parts)} part(s):")
    print()

    for i, part in enumerate(parts, 1):
        print(f"  Part {i} ({len(part)} chars):")
        print(f"  {part}")
        print()

    print("=" * 80)
    print()

# Summary
total_before = len(test_cases)
total_after = sum(len(split_long_text(c['text'])) for c in test_cases)
print(f"Summary: {total_before} inputs -> {total_after} slides")
print(f"Added {total_after - total_before} extra slide(s)")
