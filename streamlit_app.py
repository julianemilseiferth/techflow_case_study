import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

st.set_page_config(page_title="TechFlow Support Wait Analysis", layout="wide")

engine = create_engine("sqlite:///techflow.db")

df = pd.read_sql("SELECT * FROM call_records", engine)

st.title("TechFlow Solutions: Customer Support Wait Time Analysis")
st.write("This dashboard displays simulated customer support data generated for the TechFlow case study.")

col1, col2, col3 = st.columns(3)
col1.metric("Total Calls", f"{len(df):,}")
col2.metric("Average Wait Time", f"{df['wait_time_minutes'].mean():.1f} min")
col3.metric("Resolved Rate", f"{(df['resolved'].mean() * 100):.1f}%")

st.subheader("Average Wait Time by Day")
day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_wait = (
    df.groupby("day_of_week", as_index=False)["wait_time_minutes"]
    .mean()
)
day_wait["day_of_week"] = pd.Categorical(day_wait["day_of_week"], categories=day_order, ordered=True)
day_wait = day_wait.sort_values("day_of_week")
st.dataframe(day_wait, use_container_width=True)
st.bar_chart(day_wait.set_index("day_of_week"))

st.subheader("Call Volume by Hour")
hourly = df.groupby("hour_of_day", as_index=False).size().rename(columns={"size": "call_count"})
st.dataframe(hourly, use_container_width=True)
st.line_chart(hourly.set_index("hour_of_day"))

st.subheader("Call Records")
st.dataframe(df, use_container_width=True, height=420)
