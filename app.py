import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --------------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------------

st.set_page_config(
    page_title="Behavioral Alpha Engine",
    page_icon="📈",
    layout="wide"
)

# --------------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------------

st.markdown("""
<style>

body {
    background-color: #0E1117;
}

.main {
    background-color: #0E1117;
    color: white;
}

h1, h2, h3 {
    color: white;
}

.stMetric {
    background-color: #111827;
    padding: 15px;
    border-radius: 15px;
    border: 1px solid #1F2937;
}

[data-testid="metric-container"] {
    background-color: #111827;
    border-radius: 12px;
    padding: 10px;
}

.sidebar .sidebar-content {
    background-color: #111827;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------------
# LOAD DATA
# --------------------------------------------------------

df = pd.read_csv("investor_behavior_data.csv")

# CLEAN COLUMN NAMES
df.columns = df.columns.str.strip()

# --------------------------------------------------------
# CREATE SYNTHETIC FIELDS
# --------------------------------------------------------

if "Age" not in df.columns:
    df["Age"] = [25, 28, 31, 35, 40] * (len(df)//5) + [25]*(len(df)%5)

if "Income" not in df.columns:
    df["Income"] = [8, 12, 18, 25, 40] * (len(df)//5) + [10]*(len(df)%5)

if "Income_Target" not in df.columns:
    df["Income_Target"] = df["Income"] * 2.5

if "Behavioral_Score" not in df.columns:
    df["Behavioral_Score"] = [65,72,81,55,90] * (len(df)//5) + [70]*(len(df)%5)

if "Risk_Score" not in df.columns:
    df["Risk_Score"] = [3,5,7,8,4] * (len(df)//5) + [6]*(len(df)%5)

if "Portfolio_Value" not in df.columns:
    df["Portfolio_Value"] = [5,8,15,25,40] * (len(df)//5) + [10]*(len(df)%5)

if "Investor_Type" not in df.columns:
    df["Investor_Type"] = [
        "Conservative",
        "Balanced",
        "Aggressive",
        "Moderate",
        "Growth"
    ] * (len(df)//5) + ["Balanced"]*(len(df)%5)

# --------------------------------------------------------
# SIDEBAR FILTERS
# --------------------------------------------------------

st.sidebar.title("Behavioral Alpha Engine")

selected_age = st.sidebar.slider(
    "Select Age Range",
    int(df["Age"].min()),
    int(df["Age"].max()),
    (22, 40)
)

selected_income = st.sidebar.slider(
    "Select Current Income (LPA)",
    int(df["Income"].min()),
    int(df["Income"].max()),
    (5, 40)
)

selected_score = st.sidebar.slider(
    "Behavioral Score",
    0,
    100,
    (40, 100)
)

filtered_df = df[
    (df["Age"] >= selected_age[0]) &
    (df["Age"] <= selected_age[1]) &
    (df["Income"] >= selected_income[0]) &
    (df["Income"] <= selected_income[1]) &
    (df["Behavioral_Score"] >= selected_score[0]) &
    (df["Behavioral_Score"] <= selected_score[1])
]

# --------------------------------------------------------
# HEADER
# --------------------------------------------------------

st.title("Behavioral Alpha Engine")

st.subheader("AI-Powered Behavioral Wealth Intelligence Platform")

st.markdown("""
This dashboard analyzes:
- investor psychology
- emotional finance behavior
- wealth creation tendencies
- risk appetite
- portfolio patterns
- behavioral finance biases
""")

# --------------------------------------------------------
# KPI SECTION
# --------------------------------------------------------

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Investors", len(filtered_df))

with col2:
    st.metric(
        "Avg Behavioral Score",
        round(filtered_df["Behavioral_Score"].mean(),1)
    )

with col3:
    st.metric(
        "Avg Income",
        f"₹{round(filtered_df['Income'].mean(),1)}L"
    )

with col4:
    st.metric(
        "Avg Portfolio",
        f"₹{round(filtered_df['Portfolio_Value'].mean(),1)}L"
    )

# --------------------------------------------------------
# TABS
# --------------------------------------------------------

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Investor Demographics",
    "Behavioral Scorecard",
    "Income & Goals",
    "Portfolio Intelligence",
    "Survey Insights"
])

# --------------------------------------------------------
# TAB 1
# --------------------------------------------------------

with tab1:

    st.markdown("## Investor Demographics")

    col1, col2 = st.columns(2)

    with col1:

        fig_age = px.histogram(
            filtered_df,
            x="Age",
            nbins=10,
            title="Age Distribution",
            color_discrete_sequence=["#00E5FF"]
        )

        st.plotly_chart(fig_age, use_container_width=True)

    with col2:

        fig_type = px.pie(
            filtered_df,
            names="Investor_Type",
            title="Investor Type Distribution",
            hole=0.45
        )

        st.plotly_chart(fig_type, use_container_width=True)

# --------------------------------------------------------
# TAB 2
# --------------------------------------------------------

with tab2:

    st.markdown("## Behavioral Scorecard")

    col1, col2 = st.columns(2)

    with col1:

        fig_score = px.scatter(
            filtered_df,
            x="Risk_Score",
            y="Behavioral_Score",
            size="Portfolio_Value",
            color="Investor_Type",
            title="Behavioral vs Risk Mapping"
        )

        st.plotly_chart(fig_score, use_container_width=True)

    with col2:

        fig_behavior = px.histogram(
            filtered_df,
            x="Behavioral_Score",
            nbins=10,
            title="Behavioral Score Distribution",
            color_discrete_sequence=["#FF4B4B"]
        )

        st.plotly_chart(fig_behavior, use_container_width=True)

# --------------------------------------------------------
# TAB 3
# --------------------------------------------------------

with tab3:

    st.markdown("## Income & Wealth Goals")

    col1, col2 = st.columns(2)

    with col1:

        income_chart = px.scatter(
            filtered_df,
            x="Income",
            y="Income_Target",
            color="Investor_Type",
            size="Behavioral_Score",
            title="Income vs Target Wealth"
        )

        st.plotly_chart(income_chart, use_container_width=True)

    with col2:

        growth_chart = px.line(
            filtered_df.sort_values("Age"),
            x="Age",
            y="Income_Target",
            title="Target Wealth Growth by Age"
        )

        st.plotly_chart(growth_chart, use_container_width=True)

# --------------------------------------------------------
# TAB 4
# --------------------------------------------------------

with tab4:

    st.markdown("## Portfolio Intelligence")

    col1, col2 = st.columns(2)

    with col1:

        portfolio_chart = px.treemap(
            filtered_df,
            path=["Investor_Type"],
            values="Portfolio_Value",
            color="Risk_Score",
            title="Portfolio Allocation by Investor Type"
        )

        st.plotly_chart(portfolio_chart, use_container_width=True)

    with col2:

        risk_chart = px.bar(
            filtered_df,
            x="Investor_Type",
            y="Risk_Score",
            color="Investor_Type",
            title="Risk Appetite Analysis"
        )

        st.plotly_chart(risk_chart, use_container_width=True)

# --------------------------------------------------------
# TAB 5
# --------------------------------------------------------

with tab5:

    st.markdown("## Survey Findings & Investor Psychology")

    st.info("""
    KEY INSIGHTS FROM SURVEY:

    • 93.1% respondents belong to the 22–30 age bracket  
    • 55.2% prefer investing in familiar assets  
    • 48.3% wait within 3 months after losses before reinvesting  
    • 58.6% are only somewhat confident managing investments independently  
    • 51.7% expect annual returns between 8–12%  
    • 48.3% seek structured long-term wealth guidance  
    """)

    survey_chart = go.Figure(data=[
        go.Bar(
            x=[
                "Prefer Familiar Assets",
                "Need Wealth Guidance",
                "Reinvest Within 3 Months",
                "Moderate Confidence"
            ],
            y=[55.2,48.3,48.3,58.6]
        )
    ])

    survey_chart.update_layout(
        title="Behavioral Finance Survey Insights",
        template="plotly_dark"
    )

    st.plotly_chart(survey_chart, use_container_width=True)

# --------------------------------------------------------
# AI RECOMMENDATION ENGINE
# --------------------------------------------------------

st.markdown("---")

st.markdown("## AI Wealth Recommendation Engine")

risk_input = st.slider(
    "Investor Risk Appetite",
    1,
    10,
    5
)

if risk_input <= 3:

    st.success("""
    Recommended Strategy:
    - Debt-heavy allocation
    - Capital preservation
    - SIP strategy
    - Emergency reserve optimization
    """)

elif risk_input <= 7:

    st.info("""
    Recommended Strategy:
    - Hybrid investing
    - Balanced equity exposure
    - Long-term wealth creation
    - Diversified allocation
    """)

else:

    st.warning("""
    Recommended Strategy:
    - Aggressive growth investing
    - Thematic investing
    - International diversification
    - High-risk equity allocation
    """)

# --------------------------------------------------------
# FOOTER
# --------------------------------------------------------

st.markdown("---")

st.caption("""
Behavioral Alpha Engine © 2026
Institutional Behavioral Wealth Intelligence Dashboard
""")
