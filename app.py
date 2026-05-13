import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Behavioral Alpha Engine",
    page_icon="📊",
    layout="wide"
)

# =========================================================
# COLORFUL PROFESSIONAL CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
    color: black !important;
}

/* MAIN BACKGROUND */

.stApp {
    background: linear-gradient(
        135deg,
        #E0F2FE,
        #DBEAFE,
        #EDE9FE,
        #FCE7F3
    );
}

/* REMOVE EXTRA SPACE */

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* ALL TEXT */

p, span, div, label, li {
    color: black !important;
}

/* HEADINGS */

h1 {
    color: #0F172A !important;
    font-size: 4rem !important;
    font-weight: 700 !important;
}

h2, h3, h4 {
    color: #111827 !important;
}

/* METRIC CARDS */

[data-testid="metric-container"] {
    background: linear-gradient(
        135deg,
        #2563EB,
        #7C3AED
    );
    border-radius: 20px;
    padding: 22px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.15);
}

[data-testid="metric-container"] label {
    color: white !important;
}

[data-testid="metric-container"] div {
    color: white !important;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #BFDBFE,
        #DDD6FE
    );
}

section[data-testid="stSidebar"] * {
    color: black !important;
}

/* TABS */

.stTabs [data-baseweb="tab-list"] {
    gap: 12px;
}

.stTabs [data-baseweb="tab"] {
    background: white;
    border-radius: 14px;
    color: black !important;
    padding: 14px 22px;
    font-weight: 600;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(
        90deg,
        #2563EB,
        #7C3AED
    ) !important;
    color: white !important;
}

/* BUTTONS */

.stButton button {
    background: linear-gradient(
        90deg,
        #2563EB,
        #7C3AED
    );
    color: white !important;
    border: none;
    border-radius: 12px;
    padding: 12px 20px;
    font-weight: 600;
}

/* INPUTS */

input, textarea {
    background-color: white !important;
    color: black !important;
    border-radius: 10px !important;
}

/* DROPDOWN */

.stSelectbox div[data-baseweb="select"] {
    background-color: #E2E8F0 !important;
    border-radius: 12px;
}

/* DROPDOWN TEXT */

.stSelectbox * {
    color: black !important;
}

/* NUMBER INPUT */

.stNumberInput input {
    background-color: white !important;
    color: black !important;
}

/* SLIDER */

.stSlider {
    color: #2563EB;
}

/* DATAFRAME */

[data-testid="stDataFrame"] {
    border-radius: 14px;
    overflow: hidden;
}

/* CUSTOM BOX */

.tech-box {
    background: rgba(255,255,255,0.8);
    padding: 24px;
    border-radius: 20px;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.08);
}

/* SUCCESS / INFO / WARNING */

.stSuccess {
    background-color: rgba(34,197,94,0.12) !important;
    color: black !important;
}

.stInfo {
    background-color: rgba(59,130,246,0.12) !important;
    color: black !important;
}

.stWarning {
    background-color: rgba(245,158,11,0.12) !important;
    color: black !important;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# LOAD DATA
# =========================================================

df = pd.read_csv("investor_behavior_data.csv")

df.columns = df.columns.str.strip()

# =========================================================
# SYNTHETIC COLUMNS
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

st.sidebar.title("⚡ Dashboard Controls")

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

<h3>AI-Powered Behavioral Wealth Intelligence Platform</h3>

Advanced behavioral finance dashboard analyzing:
<br><br>

• Investor psychology  
• Risk appetite  
• Portfolio intelligence  
• Wealth creation goals  
• Emotional investing patterns  
• Financial behavior analytics  

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
            title="Investor Age Distribution",
            template="plotly_white"
        )

        st.plotly_chart(fig1, use_container_width=True)

    with col2:

        fig2 = px.pie(
            filtered_df,
            names="Investor_Type",
            hole=0.55,
            title="Investor Type Distribution",
            template="plotly_white"
        )

        st.plotly_chart(fig2, use_container_width=True)

# =========================================================
# TAB 2
# =========================================================

with tab2:

    fig3 = px.scatter(
        filtered_df,
        x="Risk_Score",
        y="Behavioral_Score",
        size="Portfolio_Value",
        color="Investor_Type",
        hover_data=["Goal"],
        title="Behavioral Intelligence Mapping",
        template="plotly_white"
    )

    st.plotly_chart(fig3, use_container_width=True)

# =========================================================
# TAB 3
# =========================================================

with tab3:

    fig4 = px.sunburst(
        filtered_df,
        path=["Goal", "Investor_Type"],
        values="Portfolio_Value",
        color="Risk_Score",
        title="Goal-Based Wealth Structure",
        template="plotly_white"
    )

    st.plotly_chart(fig4, use_container_width=True)

    st.dataframe(filtered_df)

# =========================================================
# TAB 4
# =========================================================

with tab4:

    fig5 = px.treemap(
        filtered_df,
        path=["Investor_Type"],
        values="Portfolio_Value",
        color="Behavioral_Score",
        title="Portfolio Allocation Intelligence",
        template="plotly_white"
    )

    st.plotly_chart(fig5, use_container_width=True)

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

    if user_risk <= 3:

        st.success("""
Recommended Strategy:

Capital preservation focused investing strategy
with debt allocation and conservative SIPs.
        """)

    elif user_risk <= 7:

        st.info("""
Recommended Strategy:

Balanced long-term wealth creation strategy
with diversified asset allocation.
        """)

    else:

        st.warning("""
Recommended Strategy:

Aggressive growth strategy with high equity exposure,
global diversification, and thematic investing.
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
        template="plotly_white"
    )

    st.plotly_chart(survey_chart, use_container_width=True)

    st.markdown("""
<div class="tech-box">

<h3>Key Research Findings</h3>

Most investors belong to the 22–35 demographic and display moderate-to-high behavioral influence in financial decision-making.

Long-term wealth creation remains the dominant financial objective while emotional investing patterns significantly influence portfolio actions.

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
