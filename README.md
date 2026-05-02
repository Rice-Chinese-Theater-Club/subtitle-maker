[English](README.md) | [简体中文](README.zh-CN.md)

# Subtitle Maker

## Introduction

A PPT subtitle generator for bilingual theater performances. Reads translation JSON files containing Chinese dialogue and English translations, then generates black-background PowerPoint slides with character names and English subtitles for live projection.

### Features

- Reads translation JSON, generates PPT subtitle slides
- Black background + white subtitles, with character pinyin name at the top
- Smart grouping: consecutive short lines from the same character merge into one slide
- Auto text splitting: translations exceeding 100 characters split at natural break points (sentences, commas, dashes)
- 16:9 widescreen aspect ratio, suitable for theater projection
- Includes a web-based Translation Manager (`translation_manager.html`) for editing, searching, and exporting translations in the browser

### Directory Structure

```
Subtitle_Maker/
├── tools/                    # Core tools
│   ├── generate_subtitles_ppt.py   # Main script: JSON → PPT
│   ├── translate_scene.py          # Create translation JSON per scene
│   ├── translation_manager.html    # Web-based translation editor
│   ├── batch_translate_remaining.py
│   ├── complete_remaining.py
│   ├── batch_complete.sh
│   └── rapid_complete.sh
├── scripts/
│   └── create_translations.py      # Batch translation mapping script
├── tests/
│   ├── analyze_length.py           # Analyze translation lengths
│   ├── test_splitting.py           # Test long text splitting
│   └── verify_ppt.py              # Verify PPT content
├── examples/
│   └── example_scene_translation.json  # Example translation JSON
├── requirements.txt
└── README.md
```

### Usage

```bash
# Install dependencies
pip install -r requirements.txt

# Generate PPT subtitles from a translation JSON
python3 tools/generate_subtitles_ppt.py translations/scene_1-4_translation.json

# Batch generate all scenes
./tools/batch_complete.sh

# Analyze translation lengths (check which lines need splitting)
python3 tests/analyze_length.py translations/scene_1-4_translation.json

# Verify PPT content
python3 tests/verify_ppt.py translations/scene_1-4_translation.json outputs/scene_1-4_subtitles.pptx
```

### Translation Manager (Web Tool)

Open `tools/translation_manager.html` directly in a browser to:
- Load a translation JSON file
- Edit English translations line by line
- Search dialogue content
- Export the modified JSON

### JSON Format

Translation files follow this schema:

```json
{
  "sceneId": "1-4",
  "sceneName": "场景中文名 (English Scene Name)",
  "totalLines": 8,
  "translations": [
    {
      "index": 0,
      "character": "角色中文名",
      "characterPinyin": "PINYIN",
      "original": "中文台词原文",
      "translation": "English translation of the line"
    }
  ]
}
```

| Field | Description |
|-------|-------------|
| `sceneId` | Scene identifier (e.g., "1-4") |
| `sceneName` | Scene name, bilingual format: "中文名 (English Name)" |
| `totalLines` | Total number of dialogue lines in the scene |
| `translations[].index` | Line index within the scene (0-based) |
| `translations[].character` | Character name in Chinese |
| `translations[].characterPinyin` | Character name in pinyin (displayed on slides) |
| `translations[].original` | Original Chinese dialogue |
| `translations[].translation` | English translation (displayed as subtitle) |

See `examples/example_scene_translation.json` for a complete example.

### Tech Stack

- Python 3
- [python-pptx](https://python-pptx.readthedocs.io/) - PowerPoint file generation
