# Subtitle Maker 字幕生成器

## 简介

双语话剧演出PPT字幕生成工具。从翻译JSON文件读取中英文台词，自动生成黑底白字的PowerPoint字幕幻灯片，用于现场演出时投影显示。

### 功能

- 读取翻译JSON文件，生成PPT字幕幻灯片
- 黑色背景 + 白色字幕，顶部显示角色拼音名
- 智能合并：同一角色的连续短台词自动合并到同一张幻灯片
- 长句自动拆分：超过100字符的译文按句号、逗号等自然断点拆分成多张幻灯片
- 16:9 宽屏比例，适合剧场投影
- 附带网页端翻译管理工具 (`translation_manager.html`)，可在浏览器中编辑、搜索、导出翻译

### 目录结构

```
Subtitle_Maker/
├── tools/                    # 核心工具
│   ├── generate_subtitles_ppt.py   # 主程序：JSON → PPT
│   ├── translate_scene.py          # 按场次创建翻译JSON
│   ├── translation_manager.html    # 网页翻译编辑器
│   ├── batch_translate_remaining.py
│   ├── complete_remaining.py
│   ├── batch_complete.sh
│   └── rapid_complete.sh
├── scripts/
│   └── create_translations.py      # 批量翻译映射脚本
├── tests/
│   ├── analyze_length.py           # 分析译文长度
│   ├── test_splitting.py           # 测试长句拆分
│   └── verify_ppt.py              # 验证PPT内容
├── examples/
│   └── example_scene_translation.json  # 示例翻译JSON
├── requirements.txt
└── README.md
```

### 使用方法

```bash
# 安装依赖
pip install -r requirements.txt

# 从翻译JSON生成PPT字幕
python3 tools/generate_subtitles_ppt.py translations/scene_1-4_translation.json

# 批量生成所有场次
./tools/batch_complete.sh

# 分析译文长度（检查哪些句子需要拆分）
python3 tests/analyze_length.py translations/scene_1-4_translation.json

# 验证PPT内容
python3 tests/verify_ppt.py translations/scene_1-4_translation.json outputs/scene_1-4_subtitles.pptx
```

### 翻译管理网页工具

直接在浏览器中打开 `tools/translation_manager.html`，可以：
- 加载翻译JSON文件
- 逐条编辑英文翻译
- 搜索台词内容
- 导出修改后的JSON

---

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

### JSON Format / JSON格式

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

### Tech Stack / 技术栈

- Python 3
- [python-pptx](https://python-pptx.readthedocs.io/) - PowerPoint file generation
