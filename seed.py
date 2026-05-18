import random
from uuid import uuid4

import numpy as np
from faker import Faker

from .database import Base, SessionLocal, engine
from .models import CallRecord

fake = Faker()
ISSUE_CATEGORIES = ["Billing", "Technical", "Service", "Account"]


def generate_call_records(num_records: int = 1000):
    call_records = []
    for _ in range(num_records):
        timestamp = fake.date_time_between(start_date="-30d", end_date="now")
        day_of_week = timestamp.strftime("%A")
        hour_of_day = timestamp.hour

        if 9 <= hour_of_day <= 17:
            wait_time = random.randint(10, 45)
        else:
            wait_time = random.randint(2, 15)

        if day_of_week in ["Monday", "Friday"]:
            wait_time += int(np.random.randint(5, 16))

        call_records.append(
            {
                "call_id": str(uuid4()),
                "customer_name": fake.name(),
                "call_timestamp": timestamp,
                "day_of_week": day_of_week,
                "hour_of_day": hour_of_day,
                "wait_time_minutes": wait_time,
                "issue_category": random.choice(ISSUE_CATEGORIES),
                "resolved": random.choice([True, False]),
            }
        )
    return call_records


def seed_database(num_records: int = 1200):
    Base.metadata.create_all(bind=engine)
    session = SessionLocal()
    try:
        session.query(CallRecord).delete()
        records = generate_call_records(num_records)
        for record in records:
            session.add(CallRecord(**record))
        session.commit()
    finally:
        session.close()


if __name__ == "__main__":
    seed_database()
