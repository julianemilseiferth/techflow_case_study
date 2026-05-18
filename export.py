from pathlib import Path

import pandas as pd
from sqlalchemy import select

from .database import SessionLocal
from .models import CallRecord


def export_call_records_csv():
    session = SessionLocal()
    try:
        records = session.execute(select(CallRecord)).scalars().all()
        df = pd.DataFrame(
            [
                {
                    "id": record.id,
                    "call_id": record.call_id,
                    "customer_name": record.customer_name,
                    "call_timestamp": record.call_timestamp,
                    "day_of_week": record.day_of_week,
                    "hour_of_day": record.hour_of_day,
                    "wait_time_minutes": record.wait_time_minutes,
                    "issue_category": record.issue_category,
                    "resolved": record.resolved,
                }
                for record in records
            ]
        )
        output_dir = Path("data")
        output_dir.mkdir(exist_ok=True)
        file_path = output_dir / "call_records.csv"
        df.to_csv(file_path, index=False)
        return file_path, df
    finally:
        session.close()


if __name__ == "__main__":
    export_call_records_csv()
