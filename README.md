# 🕷️ Automated Web Scraper & Live Interactive Dashboard

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)](https://streamlit.io/)
[![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)](https://plotly.com/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)](https://www.sqlite.org/)

An automated web data pipeline that extracts real-time metrics, persists historical records into an ACID-compliant SQLite database, and serves an interactive time-series visual analytics dashboard using **Streamlit** and **Plotly**.

---

## 🏗️ Architecture Pipeline

```text
[ Target Webpage ]
        │ (HTTP GET via Requests + SelectorLib)
        ▼
[ Parsing Engine ] ── extracts metrics using YAML rules
        │
        ▼
[ SQLite Database ] ── stores timestamped records in data.db
        │
        ▼
[ Streamlit Web App ] ── visualizes interactive trends via Plotly Express
```

---

## ✨ Features
- **Declarative Web Extraction:** Uses `selectorlib` YAML-based extraction for resilient, clean data parsing.
- **Persistent Data Store:** Automatic timestamping and historical metric tracking in SQLite.
- **Interactive UI Dashboard:** Zero-maintenance visual web dashboard with interactive zoom, hover, and panning powered by Plotly.
- **Lightweight & Fast:** Runs seamlessly in any cloud container, cron job, or local server.

---

## 🚀 Quickstart

### 1. Clone & Setup
```bash
git clone https://github.com/nabilmushfique460/Web-Scraping-Module-2.0.git
cd Web-Scraping-Module-2.0
pip install -r requirements.txt
```

### 2. Run the Data Scraper
```bash
python main.py
```

### 3. Launch the Interactive Dashboard
```bash
streamlit run webapp.py
```
Open `http://localhost:8501` to explore live time-series visualizations.

---

## 💼 Freelance & Commercial Use
Need automated data scrapers, lead generation pipelines, competitor price trackers, or custom analytics dashboards built with Python?

- **Author:** S.M. Nabil Mushfique
- **Email:** [nabilmushfique460@gmail.com](mailto:nabilmushfique460@gmail.com)
- **Services:** Custom Web Scraping, Streamlit / Plotly Dashboards, REST APIs, Automation Pipelines.
