[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md)

# 字幕生成器 (Subtitle Maker)

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

### JSON 格式

翻译文件遵循以下结构：

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

| 字段 | 说明 |
|------|------|
| `sceneId` | 场次标识（如 "1-4"） |
| `sceneName` | 场景名称，双语格式："中文名 (English Name)" |
| `totalLines` | 该场次的台词总行数 |
| `translations[].index` | 台词在场次内的索引（从0开始） |
| `translations[].character` | 角色中文名 |
| `translations[].characterPinyin` | 角色拼音名（显示在幻灯片上） |
| `translations[].original` | 中文台词原文 |
| `translations[].translation` | 英文翻译（作为字幕显示） |

完整示例见 `examples/example_scene_translation.json`。

### 技术栈

- Python 3
- [python-pptx](https://python-pptx.readthedocs.io/) - PowerPoint 文件生成
