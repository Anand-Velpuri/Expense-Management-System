import streamlit as st

def about_tab():
    st.title("📘 About This Expense Tracker")

    st.markdown("----")

    st.markdown("""
    ## 💡 What is this?

    This is a **simple and efficient expense tracker** built for personal budgeting and analysis.  
    You can **record expenses**, **analyze spending by category or month**, and **visualize trends** — all in one place.

    ---

    ## 🔧 Tech Stack

    - **Frontend**: Streamlit `v1.45.0`
    - **Backend**: FastAPI `v0.115.12`
    - **Database**: MySQL (`mysql-connector-python v9.3.0`)
    - **Data Handling**: Pandas `v2.2.3`
    - **HTTP**: Requests
    - **Testing**: Pytest `v8.3.5`
    - **Validation**: Pydantic

    ---

    ## 🚀 Features

    - 📥 Add & update expense entries
    - 📊 Category-wise analytics
    - 📅 Month-wise breakdowns
    - 📉 Interactive visualizations using Streamlit
    - ✅ Lightweight and fast backend with FastAPI

    ---

    ## 🛠️ Future Plans

    - User login & session-based tracking
    - Export reports to CSV/Excel
    - Set monthly budgets & alerts
    - Recurring expense tracking
    - Mobile responsiveness

    ---

    ## 👨‍💻 Developer

    - **Your Name**: Anand Velpuri
    - **GitHub**: [@Anand-Velpuri](https://github.com/anand-velpuri)
    - **Email**: velpurianand8005@gmail.com

    ---

    _This app is open source. Contributions, stars, and coffee are always welcome ☕✨_
    """)

    st.success("Thanks for checking out the app!")
