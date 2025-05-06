import streamlit as st
import requests
import pandas as pd

API_URL = "http://localhost:8000"

def analytics_months_tab():
    st.title("Expense Breakdown By Months")

    response = requests.get(f"{API_URL}/analytics/monthly")
    response = response.json()


    df = pd.DataFrame({
        "Month Name": [item["Month"] for item in response],
        "Total": [item["Total"] for item in response]
    }, index=[item["index"] for item in response])
    st.bar_chart(data=df.set_index("Month Name")["Total"], width=0, height=0, use_container_width=True)
    df["Total"] = df["Total"].map("{:.2f}".format)
    st.table(df)
