# TechFlow Solutions Case Study

This project simulates customer support call records for **TechFlow Solutions**, a fictional internet service provider, to identify patterns in wait times and recommend staffing changes.

## Project Structure

```
techflow_case_study/
├── app/
│   ├── __init__.py
│   ├── models.py           # SQLAlchemy CallRecord schema
│   ├── database.py         # engine, session, connection handling
│   ├── seed.py             # Faker + NumPy record generator
│   ├── export.py           # SQLite -> CSV export
│   └── streamlit_app.py    # dashboard
├── data/
│   └── call_records.csv    # exported dataset
├── memo/
│   └── business_memo.md    # one-page recommendation
├── presentation/
│   ├── techflow_findings.pptx
│   └── techflow_findings.slides.html
├── images/                 # dashboard screenshots
├── .gitignore
├── README.md
└── requirements.txt
## Setup

### 1. Create and activate a virtual environment

# Mac / Linux
python -m venv .venv && source .venv/bin/activate

# Windows
python -m venv .venv && .venv\Scripts\activate
```

### 2. Install dependencies

pip install -r requirements.txt

## Run the project

### Seed the database with 1000+ records
```python -m app.seed
```

### Export data to CSV
``python -m app.export
```

### Launch the Streamlit app
``streamlit run app/streamlit_app.py
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
