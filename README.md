# TechFlow Solutions Case Study

This project simulates customer support call records for **TechFlow Solutions**, a fictional internet service provider, to identify patterns in wait times and recommend staffing changes.

## Project Structure

```
techflow_case_study/
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── export.py
│   ├── models.py
│   ├── seed.py
│   └── streamlit_app.py
├── data/
│   └── call_records.csv
├── memo/
│   └── business_memo.md
├── presentation/
│   ├── techflow_findings.slides.html
│   └── techflow_findings.pptx
├── .gitignore
├── README.md
└── requirements.txt
```

## Setup

### 1. Create and activate a virtual environment

**Mac/Linux**
```bash
python -m venv .venv
source .venv/bin/activate
```

**Windows**
```powershell
python -m venv .venv
.venv\Scripts\activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the project

### Seed the database with 1000+ records
```bash
python -m app.seed
```

### Export data to CSV
```bash
python -m app.export
```

### Launch the Streamlit app
```bash
streamlit run app/streamlit_app.py
```

## Business problem

TechFlow Solutions needs to understand when support wait times are highest so staffing can be adjusted to reduce customer frustration, improve service quality, and protect brand reputation.

## Analysis questions

- Which day has the longest average wait time?
- What are the 3 busiest hours of the day?
- How should staffing be adjusted based on the generated patterns?

## Deliverables included

- SQLAlchemy data model for call records
- Faker + NumPy + random-based seed generator
- SQLite database integration
- CSV export for dashboarding
- Streamlit dashboard with tables and summary metrics
- One-page business memo
- Short presentation in HTML and PPTX

## Submission note

Before submitting a zip, remove the `.venv` directory. This project archive does **not** include a `.venv` folder.
