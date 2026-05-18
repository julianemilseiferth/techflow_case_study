from sqlalchemy import Boolean, Column, DateTime, Integer, String

from .database import Base


class CallRecord(Base):
    __tablename__ = "call_records"

    id = Column(Integer, primary_key=True, index=True)
    call_id = Column(String, unique=True, nullable=False, index=True)
    customer_name = Column(String, nullable=False)
    call_timestamp = Column(DateTime, nullable=False)
    day_of_week = Column(String, nullable=False)
    hour_of_day = Column(Integer, nullable=False)
    wait_time_minutes = Column(Integer, nullable=False)
    issue_category = Column(String, nullable=False)
    resolved = Column(Boolean, nullable=False)
