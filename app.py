import streamlit as st
import pandas as pd
import plotly.express as px

# ------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------

st.set_page_config(
    page_title="Behavioral Alpha Engine",
    page_icon="📈",
    layout="wide"
)

# ------------------------------------------------
# LOAD DATA
# ------------------------------------------------

investor_df = pd.read_csv("investor_behavior_data.csv")

# CLEAN COLUMN NAMES
investor_df.columns = investor_df.columns.str.strip()

# ------------------------------------------------
# HEADER
# ------------------------------------------------

st.title("Behavioral Alpha Engine")
st.subheader("AI-Powered Behavioral Wealth Intelligence Platform")

st.markdown("""
Interactive behavioral finance dashboard analyzing:
- investor psychology
- emotional investing
- risk appetite
- wealth creation patterns
- portfolio behavior
""")

# ------------------------------------------------
# SHOW DATA PREVIEW
# ------------------------------------------------

st.markdown("## Dataset Preview")

st.dataframe(investor_df.head())

# ------------------------------------------------
# COLUMN VIEWER
# ------------------------------------------------

st.markdown("## Available Dataset Columns")

st.write(list(investor_df.columns))

# ------------------------------------------------
# BASIC KPI
# ------------------------------------------------

st.markdown("## Investor Overview")

col1, col2 = st.columns(2)

with col1:
    st.metric("Total Investors", len(investor_df))

with col2:
    st.metric("Total Columns", len(investor_df.columns))

# ------------------------------------------------
# FIRST CHART
# ------------------------------------------------

first_col = investor_df.columns[0]

chart = px.histogram(
    investor_df,
    x=first_col,
    title=f"Distribution of {first_col}"
)

st.plotly_chart(chart, use_container_width=True)

# ------------------------------------------------
# FOOTER
# ------------------------------------------------

st.markdown("---")

st.caption("Behavioral Alpha Engine © 2026")
