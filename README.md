# 📈 Python 程式交易 (PythonProgramTrading)

本專案集結了 Python 程式交易的基礎開發範例，涵蓋網頁爬蟲、動態網頁處理及資料分析等核心技術。

## 🚀 核心功能與範例

1.  **🌐 基礎網頁下載** (`request.py`)
    *   使用 `requests` 套件下載網頁內容，建立資料搜集的基礎點。
2.  **🥣 排行榜資料解析** (`reponse.py`)
    *   運用 `BeautifulSoup` 套件解析 HTML 結構，精準提取排行榜等關鍵資訊。
3.  **🤖 動態網頁自動化** (`webdriver.py`)
    *   利用 `Selenium` 套件處理 JavaScript 動態渲染的網頁。
    *   ⚠️ **注意**：需至 [WebDriver 官網](https://googlechromelabs.github.io/chrome-for-testing/#stable) 下載對應 Chrome 版本的 Stable 驅動程式，以確保運行穩定，避免當機報錯。
4.  **🐼 資料合併與清理** (`pandasDemo.py`)
    *   運用 `pandas` 套件高效整合多個 DataFrame，範例包含時間、氣溫與降雨量資訊的合併處理。
