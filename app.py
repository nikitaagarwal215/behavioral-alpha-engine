import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Behavioral Alpha Engine",
    page_icon="⚡",
    layout="wide"
)

# =========================================================
# CUSTOM DARK AI CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&family=Inter:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    color: white !important;
}

/* MAIN APP */

.stApp {
    background: linear-gradient(135deg, #050816, #0B1023, #10182F);
    color: white !important;
}

/* REMOVE EXTRA SPACING */

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* TEXT */

p, span, div, label, li {
    color: white !important;
}

/* HEADINGS */

h1 {
    font-family: 'Orbitron', sans-serif;
    color: white !important;
    font-size: 4rem !important;
    letter-spacing: 2px;
}

h2, h3, h4 {
    color: white !important;
}

/* METRICS */

[data-testid="metric-container"] {
    background: linear-gradient(145deg, #111827, #1E293B);
    border: 1px solid rgba(0,229,255,0.25);
    border-radius: 18px;
    padding: 20px;
    box-shadow: 0px 0px 18px rgba(0,229,255,0.15);
}

[data-testid="metric-container"] label {
    color: #CBD5E1 !important;
}

[data-testid="metric-container"] div {
    color: white !important;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #050816, #0F172A);
    border-right: 1px solid rgba(255,255,255,0.08);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

/* TABS */

.stTabs [data-baseweb="tab-list"] {
    gap: 12px;
}

.stTabs [data-baseweb="tab"] {
    background: #111827;
    border-radius: 12px;
    color: white !important;
    padding: 14px 24px;
    font-weight: 600;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(90deg, #00E5FF, #2563EB) !important;
    color: white !important;
}

/* BUTTONS */

.stButton button {
    background: linear-gradient(90deg, #00E5FF, #2563EB);
    color: white !important;
    border: none;
    border-radius: 12px;
    padding: 12px 20px;
    font-weight: 600;
}

/* INPUTS */

input, textarea {
    background-color: #111827 !important;
    color: white !important;
}

/* SELECT BOX */

.stSelectbox div[data-baseweb="select"] {
    background-color: #111827 !important;
    color: white !important;
    border-radius: 12px;
}

/* DROPDOWN TEXT */

.stSelectbox * {
    color: white !important;
}

/* NUMBER INPUT */

.stNumberInput input {
    background-color: #111827 !important;
    color: white !important;
}

/* SLIDER */

.stSlider {
    color: #00E5FF;
}

/* DATAFRAME */

[data-testid="stDataFrame"] {
    border-radius: 14px;
    overflow: hidden;
}

/* CUSTOM BOX */

.tech-box {
    background: rgba(255,255,255,0.04);
    padding: 22px;
    border-radius: 18px;
    border: 1px solid rgba(0,229,255,0.15);
}

/* SUCCESS / INFO / WARNING */

.stSuccess {
    background-color: rgba(16,185,129,0.15) !important;
    color: white !important;
}

.stInfo {
    background-color: rgba(59,130,246,0.15) !important;
    color: white !important;
}

.stWarning {
    background-color: rgba(245,158,11,0.15) !important;
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# LOAD DATA
# =========================================================

df = pd.read_csv("investor_behavior_data.csv")

df.columns = df.columns.str.strip()

# =========================================================
# CREATE SYNTHETIC DATA
# =========================================================

if "Age" not in df.columns:
    df["Age"] = [23,25,28,31,35,40,45] * (len(df)//7) + [25]*(len(df)%7)

if "Income" not in df.columns:
    df["Income"] = [5,8,12,15,20,30,50] * (len(df)//7) + [10]*(len(df)%7)

if "Behavioral_Score" not in df.columns:
    df["Behavioral_Score"] = [65,72,78,81,69,91,75] * (len(df)//7) + [70]*(len(df)%7)

if "Risk_Score" not in df.columns:
    df["Risk_Score"] = [2,4,5,6,7,9,3] * (len(df)//7) + [5]*(len(df)%7)

if "Portfolio_Value" not in df.columns:
    df["Portfolio_Value"] = [3,6,10,18,25,40,60] * (len(df)//7) + [8]*(len(df)%7)

# =========================================================
# INVESTOR TYPES
# =========================================================

types = [
    "Conservative",
    "Balanced",
    "Growth",
    "Aggressive",
    "Elite",
    "Passive",
    "Moderate"
]

df["Investor_Type"] = [types[i % len(types)] for i in range(len(df))]

# =========================================================
# GOALS
# =========================================================

goals = [
    "Retirement",
    "Wealth Creation",
    "Passive Income",
    "Buying Property",
    "Financial Freedom",
    "Luxury Lifestyle",
    "Children Education"
]

df["Goal"] = [goals[i % len(goals)] for i in range(len(df))]

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("⚡ Control Panel")

goal_filter = st.sidebar.selectbox(
    "Financial Goal",
    df["Goal"].unique()
)

age_filter = st.sidebar.slider(
    "Age Range",
    int(df["Age"].min()),
    int(df["Age"].max()),
    (22,45)
)

income_filter = st.sidebar.slider(
    "Income Range (LPA)",
    int(df["Income"].min()),
    int(df["Income"].max()),
    (5,50)
)

risk_filter = st.sidebar.slider(
    "Risk Appetite",
    1,
    10,
    (2,9)
)

filtered_df = df[
    (df["Goal"] == goal_filter) &
    (df["Age"] >= age_filter[0]) &
    (df["Age"] <= age_filter[1]) &
    (df["Income"] >= income_filter[0]) &
    (df["Income"] <= income_filter[1]) &
    (df["Risk_Score"] >= risk_filter[0]) &
    (df["Risk_Score"] <= risk_filter[1])
]

# =========================================================
# HEADER
# =========================================================

st.title("Behavioral Alpha Engine")

st.markdown("""
<div class="tech-box">

### AI-Powered Behavioral Wealth Intelligence Platform

Advanced behavioral finance dashboard analyzing investor psychology,
risk appetite, wealth goals, portfolio intelligence,
and emotional investing patterns.

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =========================================================
# KPI SECTION
# =========================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Total Investors", len(filtered_df))

with c2:
    st.metric(
        "Avg Behavioral Score",
        round(filtered_df["Behavioral_Score"].mean(),1)
    )

with c3:
    st.metric(
        "Avg Income",
        f"₹{round(filtered_df['Income'].mean(),1)}L"
    )

with c4:
    st.metric(
        "Avg Portfolio",
        f"₹{round(filtered_df['Portfolio_Value'].mean(),1)}L"
    )

# =========================================================
# TABS
# =========================================================

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 Demographics",
    "🧠 Behavioral Scorecard",
    "🎯 Financial Goals",
    "💼 Portfolio Intelligence",
    "🤖 AI Advisory",
    "📈 Survey Insights"
])

# =========================================================
# TAB 1
# =========================================================

with tab1:

    col1, col2 = st.columns(2)

    with col1:

        fig1 = px.histogram(
            filtered_df,
            x="Age",
            color="Investor_Type",
            template="plotly_dark",
            title="Investor Age Distribution"
        )

        fig1.update_layout(
            paper_bgcolor="#0B1023",
            plot_bgcolor="#0B1023",
            font_color="white"
        )

        st.plotly_chart(fig1, use_container_width=True)

    with col2:

        fig2 = px.pie(
            filtered_df,
            names="Investor_Type",
            hole=0.55,
            template="plotly_dark",
            title="Investor Type Distribution"
        )

        fig2.update_layout(
            paper_bgcolor="#0B1023",
            font_color="white"
        )

        st.plotly_chart(fig2, use_container_width=True)

# =========================================================
# TAB 2
# =========================================================

with tab2:

    col1, col2 = st.columns(2)

    with col1:

        fig3 = px.scatter(
            filtered_df,
            x="Risk_Score",
            y="Behavioral_Score",
            size="Portfolio_Value",
            color="Investor_Type",
            hover_data=["Goal"],
            template="plotly_dark",
            title="Behavioral Intelligence Mapping"
        )

        fig3.update_layout(
            paper_bgcolor="#0B1023",
            plot_bgcolor="#0B1023",
            font_color="white"
        )

        st.plotly_chart(fig3, use_container_width=True)

    with col2:

        fig4 = px.bar(
            filtered_df,
            x="Investor_Type",
            y="Behavioral_Score",
            color="Investor_Type",
            template="plotly_dark",
            title="Behavioral Scorecard"
        )

        fig4.update_layout(
            paper_bgcolor="#0B1023",
            plot_bgcolor="#0B1023",
            font_color="white"
        )

        st.plotly_chart(fig4, use_container_width=True)

# =========================================================
# TAB 3
# =========================================================

with tab3:

    st.subheader("Goal-Based Wealth Intelligence")

    fig5 = px.sunburst(
        filtered_df,
        path=["Goal", "Investor_Type"],
        values="Portfolio_Value",
        color="Risk_Score",
        template="plotly_dark",
        title="Goal-Oriented Wealth Structure"
    )

    fig5.update_layout(
        paper_bgcolor="#0B1023",
        font_color="white"
    )

    st.plotly_chart(fig5, use_container_width=True)

    st.markdown("""
<div class="tech-box">

### Financial Goal Intelligence

This section analyzes investor wealth objectives,
income levels, portfolio alignment,
and behavioral decision-making patterns
across different financial goals.

</div>
""", unsafe_allow_html=True)

    st.dataframe(filtered_df)

# =========================================================
# TAB 4
# =========================================================

with tab4:

    col1, col2 = st.columns(2)

    with col1:

        fig6 = px.treemap(
            filtered_df,
            path=["Investor_Type"],
            values="Portfolio_Value",
            color="Behavioral_Score",
            template="plotly_dark",
            title="Portfolio Allocation Intelligence"
        )

        fig6.update_layout(
            paper_bgcolor="#0B1023",
            font_color="white"
        )

        st.plotly_chart(fig6, use_container_width=True)

    with col2:

        fig7 = px.line(
            filtered_df.sort_values("Age"),
            x="Age",
            y="Portfolio_Value",
            color="Investor_Type",
            markers=True,
            template="plotly_dark",
            title="Portfolio Growth Curve"
        )

        fig7.update_layout(
            paper_bgcolor="#0B1023",
            plot_bgcolor="#0B1023",
            font_color="white"
        )

        st.plotly_chart(fig7, use_container_width=True)

# =========================================================
# TAB 5
# =========================================================

with tab5:

    st.subheader("AI Recommendation Engine")

    user_goal = st.selectbox(
        "Select Primary Goal",
        goals
    )

    user_risk = st.slider(
        "Risk Appetite",
        1,
        10,
        5
    )

    wealth_target = st.number_input(
        "Target Wealth Goal (₹ Lakhs)",
        value=100
    )

    if user_risk <= 3:

        st.success("""
### Recommended Strategy

Capital preservation focused strategy with debt allocation,
gold ETFs, conservative SIP investing,
and emergency reserve optimization.
        """)

    elif user_risk <= 7:

        st.info("""
### Recommended Strategy

Balanced wealth creation strategy involving
hybrid mutual funds, SIP diversification,
and long-term portfolio compounding.
        """)

    else:

        st.warning("""
### Recommended Strategy

Aggressive growth strategy including
high-growth equities, thematic investing,
global diversification, and startup exposure.
        """)

# =========================================================
# TAB 6
# =========================================================

with tab6:

    survey_chart = go.Figure(data=[
        go.Bar(
            x=[
                "Need Guidance",
                "Fear Volatility",
                "Prefer Familiar Assets",
                "Long-Term Investors"
            ],
            y=[48,61,55,72]
        )
    ])

    survey_chart.update_layout(
        title="Behavioral Survey Insights",
        template="plotly_dark",
        paper_bgcolor="#0B1023",
        plot_bgcolor="#0B1023",
        font_color="white"
    )

    st.plotly_chart(survey_chart, use_container_width=True)

    st.markdown("""
<div class="tech-box">

### Key Research Findings

Most investors belong to the 22–35 demographic and display moderate-to-high behavioral influence in financial decision-making.

Long-term wealth creation remains the dominant financial objective while emotional investing patterns significantly impact portfolio actions.

</div>
""", unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption("""
Behavioral Alpha Engine © 2026  
AI + Behavioral Finance Research Platform
""")
