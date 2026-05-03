[English](README.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md)

# 字幕產生器 (Subtitle Maker)

## 簡介

雙語話劇演出 PPT 字幕產生工具。從翻譯 JSON 檔案讀取中英文台詞，自動產生黑底白字的 PowerPoint 字幕投影片，用於現場演出時投影顯示。

### 功能

- 讀取翻譯 JSON 檔案，產生 PPT 字幕投影片
- 黑色背景 + 白色字幕，頂部顯示角色拼音名
- 智慧合併：同一角色的連續短台詞自動合併到同一張投影片
- 長句自動拆分：超過 100 字元的譯文按句號、逗號等自然斷點拆分成多張投影片
- 16:9 寬螢幕比例，適合劇場投影
- 附帶網頁端翻譯管理工具 (`translation_manager.html`)，可在瀏覽器中編輯、搜尋、匯出翻譯

### 目錄結構

```
subtitle-maker/
├── tools/                    # 核心工具
│   ├── generate_subtitles_ppt.py   # 主程式：JSON → PPT
│   ├── translate_scene.py          # 按場次建立翻譯 JSON
│   ├── translation_manager.html    # 網頁翻譯編輯器
│   ├── batch_translate_remaining.py
│   ├── complete_remaining.py
│   ├── batch_complete.sh
│   └── rapid_complete.sh
├── scripts/
│   └── create_translations.py      # 批次翻譯對應指令碼
├── tests/
│   ├── analyze_length.py           # 分析譯文長度
│   ├── test_splitting.py           # 測試長句拆分
│   └── verify_ppt.py              # 驗證 PPT 內容
├── examples/
│   └── example_scene_translation.json  # 範例翻譯 JSON
├── requirements.txt
└── README.md
```

### 使用方法

```bash
# 安裝依賴
pip install -r requirements.txt

# 從翻譯 JSON 產生 PPT 字幕
python3 tools/generate_subtitles_ppt.py translations/scene_1-4_translation.json

# 批次產生所有場次
./tools/batch_complete.sh

# 分析譯文長度（檢查哪些句子需要拆分）
python3 tests/analyze_length.py translations/scene_1-4_translation.json

# 驗證 PPT 內容
python3 tests/verify_ppt.py translations/scene_1-4_translation.json outputs/scene_1-4_subtitles.pptx
```

### 翻譯管理網頁工具

直接在瀏覽器中開啟 `tools/translation_manager.html`，可以：
- 載入翻譯 JSON 檔案
- 逐條編輯英文翻譯
- 搜尋台詞內容
- 匯出修改後的 JSON

### JSON 格式

翻譯檔案遵循以下結構：

```json
{
  "sceneId": "1-4",
  "sceneName": "場景中文名 (English Scene Name)",
  "totalLines": 8,
  "translations": [
    {
      "index": 0,
      "character": "角色中文名",
      "characterPinyin": "PINYIN",
      "original": "中文台詞原文",
      "translation": "English translation of the line"
    }
  ]
}
```

| 欄位 | 說明 |
|------|------|
| `sceneId` | 場次識別碼（如 "1-4"） |
| `sceneName` | 場景名稱，雙語格式：「中文名 (English Name)」 |
| `totalLines` | 該場次的台詞總行數 |
| `translations[].index` | 台詞在場次內的索引（從 0 開始） |
| `translations[].character` | 角色中文名 |
| `translations[].characterPinyin` | 角色拼音名（顯示在投影片上） |
| `translations[].original` | 中文台詞原文 |
| `translations[].translation` | 英文翻譯（作為字幕顯示） |

完整範例見 `examples/example_scene_translation.json`。

### 技術棧

- Python 3
- [python-pptx](https://python-pptx.readthedocs.io/) - PowerPoint 檔案產生
