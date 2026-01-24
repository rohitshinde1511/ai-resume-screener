# AI Resume Screener with JD Fit Scoring & Bias Signals

An end-to-end **AI-powered resume screening system** that compares a candidate’s resume with a job description to generate a match score, highlight skill gaps, and surface potential bias signals — delivered through a clean API-first design.

This project focuses on **practical NLP + responsible AI**, not just text similarity.

---

## 🚀 What This Project Does

Given:
- A **resume text**
- A **job description text**

The system returns:
- Resume ↔ JD **similarity score**
- **Matched skills**
- **Missing skills**
- **Bias-related signals** (heuristic flags)
- A **clear natural-language explanation**

---

## 🎯 Why This Matters

Recruiters and ATS systems often:
- Miss qualified candidates due to keyword mismatch
- Lack transparency in screening decisions
- Ignore bias risks in automated filtering

This project demonstrates how **AI screening can be explainable, testable, and responsible**.

---

## 🧠 Core Capabilities

- Semantic similarity using sentence embeddings
- Skill extraction and gap analysis
- Bias signal detection (rule-based heuristics)
- Human-readable explanation generation
- REST API with schema validation
- Fully testable modular architecture

---

## 🏗️ Project Architecture

ai-resume-screener/
│
├── app/
│ └── main.py # API entry point (FastAPI runner)
│
├── src/
│ ├── api.py # API routes and request/response models
│ ├── embeddings.py # Resume ↔ JD similarity logic
│ ├── skills.py # Skill extraction & gap analysis
│ ├── bias.py # Bias signal detection
│ ├── explain.py # Natural-language explanation generator
│ ├── extract.py # Text preprocessing utilities
│ └── validate.py # Input validation helpers
│
├── data/
│ └── skills_master.txt # Reference skill vocabulary
│
├── tests/
│ ├── test_similarity.py
│ ├── test_skills.py
│ ├── test_bias.py
│ ├── test_explain.py
│ └── test_extract.py
│
├── requirements.txt
├── README.md
└── .gitignore


---

## 🔌 API Overview

### Endpoint
POST /screen


### Request Body (JSON)
```json
{
  "resume_text": "Experienced Python developer with SQL and FastAPI...",
  "jd_text": "Looking for a data analyst with Python, SQL, Docker..."
}

### Response (JSON)

{
  "similarity_score": 64.1,
  "matched_skills": ["python", "sql", "docker"],
  "missing_skills": ["cloud"],
  "bias_signals": [],
  "explanation": "The resume shows a similarity score of 64.1 with the job description..."
}

▶️ How to Run Locally :

1. Create virtual environment

python -m venv venv

2. Activate it

Windows

venv\Scripts\activate

macOS / Linux

source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Start the API server

uvicorn src.api:app --reload

5. Open API docs

http://127.0.0.1:8000/docs

🧪 Run Tests

pytest



All core components are unit-tested for correctness and stability.

🧰 Tech Stack :

Python

FastAPI

Sentence Transformers

Scikit-learn

NumPy

PyTest

Uvicorn

🔒 Notes on Bias Detection

Bias detection in this project is heuristic and exploratory, intended to:

(1) Surface potential risk signals

(2) Encourage human review

(3) Demonstrate responsible AI practices

It is not a final fairness or compliance system.

📌 Project Status

# MVP complete

# API-first architecture

# UI optional (can be added via Streamlit or frontend later)

# Designed to be extended with LLMs or vector databases

👤 Author

Rohit Shinde
Aspiring Data Analyst / Data Scientist
Focused on real-world, deployable ML systems