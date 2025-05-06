import streamlit as st
from add_update_ui import add_update_tab
from analytics_by_category import analytics_category_tab
from analytics_by_months import analytics_months_tab
from about import about_tab

st.set_page_config(page_title="Expense Manager")
st.title("💸 Expense Management System")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "➕ Add/Update",
    "📊 Analytics By Category",
    "📅 Analytics By Months",
    "ℹ️ About"
])

with tab1:
    add_update_tab()

with tab2:
    analytics_category_tab()

with tab3:
    analytics_months_tab()

with tab4:
    about_tab()

# Footer
st.markdown("---")
st.markdown(
    "<div style='text-align: center; color: gray;'>"
    "Made with ❤️ by <strong>Anand Velpuri</strong>"
    "</div>",
    unsafe_allow_html=True
)
