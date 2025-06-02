# 🌡️ Random Yearly Temperature Calendar API + Frontend

This project is a fun experiment I built to **practice recently learned NumPy** concepts by generating synthetic temperature data. It includes:
- A **Flask API** that returns daily temperatures for each month using NumPy.
- A simple **HTML frontend** that visualizes the data in a calendar-like layout.

---
![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-2.3-lightgrey?logo=flask)
![NumPy](https://img.shields.io/badge/Numpy-1.24-orange?logo=numpy)
![Render](https://img.shields.io/badge/Hosted%20on-Render-3c3c3c?logo=render)
![Status](https://img.shields.io/badge/API-Live-brightgreen)

---
## 🔗 Live Demo

- **API:** [https://temperature-api-j8nv.onrender.com/temperature-data](https://temperature-api-j8nv.onrender.com/temperature-data)
- **Frontend Preview:** [https://htmlpreview.github.io/?https://github.com/ronaksarvaya/temperature-api/blob/main/sample.html](https://htmlpreview.github.io/?https://github.com/ronaksarvaya/temperature-api/blob/main/sample.html) 

---

## 🚀 Features

- Random temperature generation for each day (range: 26°C – 41°C)
- Organized month-wise temperature data
- API response structure maintains `Jan → Dec` order using `OrderedDict`
- Simple frontend that displays the temperature data in calendar format

## 🧾 API Endpoint
GET /temperature-data
