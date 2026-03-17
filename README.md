# 🔐 Network Security — Phishing URL Detection System

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python)](https://www.python.org/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Atlas-green?logo=mongodb)](https://www.mongodb.com/atlas)
[![Docker](https://img.shields.io/badge/Docker-Supported-blue?logo=docker)](https://www.docker.com/)
[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-black?logo=github-actions)](https://github.com/features/actions)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

> A production-ready MLOps pipeline for detecting phishing URLs using machine learning — with MongoDB Atlas as the data layer, modular Python packaging, structured logging, and a CI/CD workflow via GitHub Actions.

---

## 📌 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Dataset](#-dataset)
- [Architecture](#-architecture)
- [Getting Started](#-getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Environment Variables](#environment-variables)
- [Usage](#-usage)
  - [Push Data to MongoDB](#1-push-data-to-mongodb)
- [CI/CD Pipeline](#-cicd-pipeline)
- [Tech Stack](#-tech-stack)
- [Author](#-author)

---

## 🧠 Overview

This project builds a **phishing URL detection system** as a full MLOps pipeline. It ingests a labeled phishing dataset (30 URL-based features), stores it in **MongoDB Atlas**, and provides a structured, modular Python codebase ready for training, evaluation, and deployment.

The system is designed following software engineering best practices — custom exception handling, structured logging, environment-based configuration, and Docker-ready packaging.

---

## ✨ Features

- ✅ **Phishing Detection** — 30-feature URL analysis dataset (IP, SSL, domain age, redirects, etc.)
- ✅ **MongoDB Integration** — CSV → JSON → MongoDB Atlas ingestion pipeline
- ✅ **Custom Exception Handling** — File name + line number tracebacks for every error
- ✅ **Structured Logging** — Timestamped log files auto-generated per run
- ✅ **Modular Package** — Installable Python package via `setup.py`
- ✅ **Docker Support** — Containerized for consistent environments
- ✅ **CI/CD Ready** — GitHub Actions workflow included

---

## 📁 Project Structure

```
Network-Security-project/
│
├── Network_Data/
│   └── phisingData.csv          # Raw phishing URL dataset (30 features + label)
│
├── networksecurity/             # Core Python package
│   ├── cloud/                   # Cloud utilities (S3, etc.)
│   ├── components/              # ML pipeline components (ingestion, training, etc.)
│   ├── constant/                # Project-wide constants
│   ├── entity/                  # Config & artifact dataclass definitions
│   ├── exception/
│   │   └── exception.py         # Custom NetworkSecurityException
│   ├── logging/
│   │   └── logger.py            # Timestamped file logger
│   ├── pipeline/                # Training & prediction pipelines
│   └── utils/                   # Shared utility functions
│
├── logs/                        # Auto-generated timestamped log files
├── .github/workflows/
│   └── main.yml                 # CI/CD pipeline (GitHub Actions)
│
├── push_data.py                 # Script to ingest CSV → MongoDB Atlas
├── test_mongo.py                # MongoDB connection test
├── Dockerfile                   # Docker image definition
├── setup.py                     # Package setup & dependency loader
├── requirements.txt             # Python dependencies
└── .env                         # Environment variables (not committed)
```

---

## 📊 Dataset

The dataset (`Network_Data/phisingData.csv`) contains **30 URL-based features** used to classify URLs as phishing (`-1`) or legitimate (`1`).

| Feature Category | Examples |
|---|---|
| **URL-based** | `having_IP_Address`, `URL_Length`, `Shortining_Service`, `having_At_Symbol` |
| **Domain-based** | `Domain_registeration_length`, `age_of_domain`, `DNSRecord`, `Prefix_Suffix` |
| **Security** | `SSLfinal_State`, `HTTPS_token`, `Favicon`, `port` |
| **HTML/JS** | `Iframe`, `popUpWidnow`, `RightClick`, `on_mouseover`, `Redirect` |
| **External** | `web_traffic`, `Page_Rank`, `Google_Index`, `Links_pointing_to_page` |
| **Label** | `Result` → `-1` (phishing) or `1` (legitimate) |

---

## 🏗️ Architecture

```
CSV Dataset
    │
    ▼
push_data.py
    │  reads CSV → converts to JSON records
    ▼
MongoDB Atlas  (Database: BISHAL / Collection: NetworkData)
    │
    ▼
networksecurity/
  ├── components/   ← Data Ingestion, Validation, Transformation, Training
  ├── pipeline/     ← Training Pipeline / Prediction Pipeline
  ├── entity/       ← Config & Artifact entities
  └── cloud/        ← Model storage (S3 / cloud)
    │
    ▼
Trained Model → Prediction API
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- MongoDB Atlas account (free tier works)
- Docker (optional)
- Git

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/bishalth28/Network-Security-project.git
cd Network-Security-project

# 2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate        # Linux/macOS
venv\Scripts\activate           # Windows

# 3. Install the package and dependencies
pip install -r requirements.txt
pip install -e .
```

### Environment Variables

Create a `.env` file in the project root:

```env
MONGO_DB_URL=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/?retryWrites=true&w=majority
```

> ⚠️ Never commit your `.env` file. It's already in `.gitignore`.

---

## 💻 Usage

### 1. Push Data to MongoDB

Ingests `Network_Data/phisingData.csv` into your MongoDB Atlas collection.

```bash
python push_data.py
```

Expected output:
```
mongodb+srv://...
[{'having_IP_Address': -1, 'URL_Length': 1, ...}, ...]
11055   # number of records inserted
```

### 2. Test MongoDB Connection

```bash
python test_mongo.py
```

### 3. Run with Docker

```bash
docker build -t network-security .
docker run --env-file .env network-security
```

---

## ⚙️ CI/CD Pipeline

GitHub Actions workflow (`.github/workflows/main.yml`) automates:

- Code checkout & environment setup
- Dependency installation
- Build and test validation
- Docker image build & push (if configured)

Triggered on every push to `main`.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| Data Storage | MongoDB Atlas (`pymongo`) |
| Data Processing | Pandas, NumPy |
| Configuration | `python-dotenv` |
| Packaging | `setuptools` |
| Containerization | Docker |
| CI/CD | GitHub Actions |
| SSL/TLS | `certifi` |

---

## 👤 Author

**Bishal Thapa**
📧 [btbishal09@gmail.com](mailto:btbishal09@gmail.com)
🐙 [@bishalth28](https://github.com/bishalth28)

---

> ⭐ If you found this project helpful, consider giving it a star on GitHub!
