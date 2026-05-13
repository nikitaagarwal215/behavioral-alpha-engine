import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Behavioral Alpha Engine",
    page_icon="📈",
    layout="wide"
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>
.main {
    background-color: #0E1117;
    color: white;
}

[data-testid="stMetricValue"] {
    font-size: 28px;
    color: #00E5FF;
}

h1, h2, h3 {
    color: white;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.css-1d391kg {
    background-color: #111827;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

investor_df = pd.read_csv("investor_behavior_data.csv")
scorecard_df = pd.read_csv("behavioral_scorecard.csv")
portfolio_df = pd.read_csv("portfolio_simulation.csv")

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

st.sidebar.title("Behavioral Alpha Engine")

selected_age = st.sidebar.multiselect(
    "Select Age Group",
    investor_df["Age_Group"].unique(),
    default=investor_df["Age_Group"].unique()
)

selected_goal = st.sidebar.multiselect(
    "Select Financial Goal",
    investor_df["Primary_Goal"].unique(),
    default=investor_df["Primary_Goal"].unique()
)

filtered_df = investor_df[
    (investor_df["Age_Group"].isin(selected_age)) &
    (investor_df["Primary_Goal"].isin(selected_goal))
]

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.title("Behavioral Alpha Engine")
st.subheader("AI-Powered Behavioral Wealth Intelligence Platform")

st.markdown("""
This dashboard analyzes investor psychology, behavioral finance biases,
risk appetite, emotional investing patterns, and wealth management tendencies.
""")

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Investors", len(filtered_df))

with col2:
    avg_risk = round(filtered_df["Risk_Tolerance_Score"].mean(), 2)
    st.metric("Avg Risk Score", avg_risk)

with col3:
    avg_conf = round(filtered_df["Confidence_Score"].mean(), 2)
    st.metric("Avg Confidence", avg_conf)

with col4:
    avg_return = round(filtered_df["Expected_Return"].mean(), 2)
    st.metric("Expected Return %", f"{avg_return}%")

# ---------------------------------------------------
# INVESTOR DEMOGRAPHICS
# ---------------------------------------------------

st.markdown("## Investor Demographics")

col1, col2 = st.columns(2)

with col1:
    age_chart = px.pie(
        filtered_df,
        names="Age_Group",
        title="Age Group Distribution",
        hole=0.45
    )
    st.plotly_chart(age_chart, use_container_width=True)

with col2:
    profession_chart = px.histogram(
        filtered_df,
        x="Profession",
        color="Profession",
        title="Profession Distribution"
    )
    st.plotly_chart(profession_chart, use_container_width=True)

# ---------------------------------------------------
# FINANCIAL GOALS
# ---------------------------------------------------

st.markdown("## Financial Goals & Investment Psychology")

col1, col2 = st.columns(2)

with col1:
    goal_chart = px.pie(
        filtered_df,
        names="Primary_Goal",
        title="Primary Financial Goal"
    )
    st.plotly_chart(goal_chart, use_container_width=True)

with col2:
    diversification_chart = px.histogram(
        filtered_df,
        x="Portfolio_Diversification",
        color="Portfolio_Diversification",
        title="Portfolio Diversification"
    )
    st.plotly_chart(diversification_chart, use_container_width=True)

# ---------------------------------------------------
# BEHAVIORAL BIAS ANALYSIS
# ---------------------------------------------------

st.markdown("## Behavioral Bias Analysis")

col1, col2 = st.columns(2)

with col1:
    herd_chart = px.pie(
        filtered_df,
        names="Social_Influence",
        title="Influence of Social Investing"
    )
    st.plotly_chart(herd_chart, use_container_width=True)

with col2:
    confidence_chart = px.histogram(
        filtered_df,
        x="Confidence_Score",
        nbins=5,
        title="Investment Confidence Distribution"
    )
    st.plotly_chart(confidence_chart, use_container_width=True)

# ---------------------------------------------------
# LOSS AVERSION ANALYSIS
# ---------------------------------------------------

st.markdown("## Loss Aversion & Emotional Investing")

col1, col2 = st.columns(2)

with col1:
    loss_chart = px.pie(
        filtered_df,
        names="Loss_Reaction",
        title="Reaction to Portfolio Decline"
    )
    st.plotly_chart(loss_chart, use_container_width=True)

with col2:
    reinvest_chart = px.histogram(
        filtered_df,
        x="Reinvestment_Timeframe",
        color="Reinvestment_Timeframe",
        title="Reinvestment Recovery Time"
    )
    st.plotly_chart(reinvest_chart, use_container_width=True)

# ---------------------------------------------------
# PORTFOLIO ANALYSIS
# ---------------------------------------------------

st.markdown("## Portfolio Simulation Analysis")

portfolio_chart = px.scatter(
    portfolio_df,
    x="Risk_Score",
    y="Expected_Return",
    size="Portfolio_Value",
    color="Investor_Type",
    hover_name="Investor_ID",
    title="Risk vs Return Portfolio Mapping"
)

st.plotly_chart(portfolio_chart, use_container_width=True)

# ---------------------------------------------------
# INVESTOR SEGMENTATION
# ---------------------------------------------------

st.markdown("## Investor Persona Segmentation")

persona_chart = px.treemap(
    filtered_df,
    path=["Investor_Persona"],
    values="Portfolio_Value",
    color="Risk_Tolerance_Score",
    title="Investor Persona Mapping"
)

st.plotly_chart(persona_chart, use_container_width=True)

# ---------------------------------------------------
# ADVISORY ENGINE
# ---------------------------------------------------

st.markdown("## AI Advisory Recommendation Engine")

risk_score = st.slider(
    "Select Investor Risk Appetite",
    1,
    10,
    5
)

if risk_score <= 3:
    st.success("""
    Recommended Strategy:
    - Debt-heavy allocation
    - SIP investing
    - Emergency reserve optimization
    - Capital preservation strategy
    """)

elif risk_score <= 7:
    st.info("""
    Recommended Strategy:
    - Hybrid portfolio
    - Equity + debt diversification
    - Long-term wealth creation
    - Balanced asset allocation
    """)

else:
    st.warning("""
    Recommended Strategy:
    - Aggressive equity exposure
    - High-growth thematic investing
    - International diversification
    - Alternative assets exposure
    """)

# ---------------------------------------------------
# SURVEY INSIGHTS
# ---------------------------------------------------

st.markdown("## Key Survey Insights")

st.info("""
• 93.1% respondents belong to the 22–30 age bracket  
• 55.2% prefer investing in familiar assets despite diversification risks  
• 48.3% respondents wait within 3 months after losses before reinvesting  
• 58.6% feel only somewhat confident managing investments independently  
• 51.7% expect annual returns between 8–12%  
• 48.3% seek structured long-term wealth guidance  
""")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown("---")

st.caption("""
Behavioral Alpha Engine © 2026  
AI-Powered Behavioral Finance Intelligence Dashboard
""")
