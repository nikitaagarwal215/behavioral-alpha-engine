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

/* CUSTOM BOX */

.tech-box {
    background: rgba(255,255,255,0.8);
    padding: 24px;
    border-radius: 20px;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.08);
}

/* DATAFRAME */

[data-testid="stDataFrame"] {
    border-radius: 14px;
    overflow: hidden;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# LOAD DATA
# =========================================================

df = pd.read_csv("investor_behavior_data.csv")

df.columns = df.columns.str.strip()

# =========================================================
# SYNTHETIC DATA
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
# ADD BEHAVIORAL SCORES
# =========================================================

df["Loss_Aversion"] = [78,65,88,70,60,92,55] * (len(df)//7) + [70]*(len(df)%7)
df["Home_Bias"] = [55,72,64,81,69,50,75] * (len(df)//7) + [65]*(len(df)%7)
df["Overconfidence"] = [66,82,74,91,58,80,62] * (len(df)//7) + [68]*(len(df)%7)
df["FOMO_Score"] = [72,85,69,78,64,88,59] * (len(df)//7) + [70]*(len(df)%7)

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
# SIDEBAR FILTERS
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

This dashboard helps wealth managers understand investor psychology,
risk appetite, emotional investing patterns,
and portfolio suitability in real time.

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

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "📊 Demographics",
    "🧠 Behavioral Scorecard",
    "🎯 Financial Goals",
    "💼 Portfolio Intelligence",
    "⚖ Balanced Scorecard",
    "🤖 AI Advisory",
    "📈 Survey Insights"
])

# =========================================================
# TAB 1
# =========================================================

with tab1:

    fig1 = px.histogram(
        filtered_df,
        x="Age",
        color="Investor_Type",
        title="Investor Age Distribution",
        template="plotly_white"
    )

    st.plotly_chart(fig1, use_container_width=True)

# =========================================================
# TAB 2
# =========================================================

with tab2:

    st.subheader("Behavioral Bias Scorecard")

    bias_scores = pd.DataFrame({
        "Bias": [
            "Loss Aversion",
            "Home Bias",
            "Overconfidence",
            "FOMO"
        ],
        "Score": [
            filtered_df["Loss_Aversion"].mean(),
            filtered_df["Home_Bias"].mean(),
            filtered_df["Overconfidence"].mean(),
            filtered_df["FOMO_Score"].mean()
        ]
    })

    fig2 = px.bar(
        bias_scores,
        x="Bias",
        y="Score",
        color="Bias",
        title="Average Behavioral Bias Scores",
        template="plotly_white"
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("""
<div class="tech-box">

<h3>Business Interpretation</h3>

Higher loss aversion indicates emotional panic-selling tendencies.
High overconfidence suggests excessive trading behavior.
Strong home bias reflects preference toward familiar assets.
Elevated FOMO scores indicate trend-chasing investment patterns.

</div>
""", unsafe_allow_html=True)

# =========================================================
# TAB 3
# =========================================================

with tab3:

    fig3 = px.sunburst(
        filtered_df,
        path=["Goal", "Investor_Type"],
        values="Portfolio_Value",
        color="Risk_Score",
        title="Goal-Based Wealth Structure",
        template="plotly_white"
    )

    st.plotly_chart(fig3, use_container_width=True)

# =========================================================
# TAB 4
# =========================================================

with tab4:

    fig4 = px.scatter(
        filtered_df,
        x="Risk_Score",
        y="Portfolio_Value",
        color="Investor_Type",
        size="Behavioral_Score",
        title="Risk vs Portfolio Intelligence",
        template="plotly_white"
    )

    st.plotly_chart(fig4, use_container_width=True)

    st.markdown("""
<div class="tech-box">

<h3>Portfolio Intelligence</h3>

This section helps RuDo Wealth identify
which investor categories are overexposed to risk,
under-diversified, or emotionally driven.

</div>
""", unsafe_allow_html=True)

# =========================================================
# TAB 5
# =========================================================

with tab5:

    st.subheader("Balanced Wealth Scorecard")

    scorecard = pd.DataFrame({
        "Metric": [
            "Behavioral Stability",
            "Portfolio Diversification",
            "Risk Alignment",
            "Goal Clarity",
            "Investment Discipline"
        ],
        "Score": [72,68,75,80,64]
    })

    fig5 = px.bar(
        scorecard,
        x="Metric",
        y="Score",
        color="Score",
        title="Balanced Wealth Performance Scorecard",
        template="plotly_white"
    )

    st.plotly_chart(fig5, use_container_width=True)

    st.markdown("""
<div class="tech-box">

<h3>Strategic Use for RuDo Wealth</h3>

The balanced scorecard enables advisors
to identify weaknesses in client behavior,
improve retention, personalize financial advice,
and optimize long-term wealth outcomes.

</div>
""", unsafe_allow_html=True)

# =========================================================
# TAB 6
# =========================================================

with tab6:

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

Conservative allocation with debt instruments,
gold exposure, and low-volatility SIPs.
        """)

    elif user_risk <= 7:

        st.info("""
Recommended Strategy:

Balanced wealth creation through diversified
mutual funds and long-term investing.
        """)

    else:

        st.warning("""
Recommended Strategy:

Aggressive growth strategy involving equities,
global diversification, and thematic investing.
        """)

# =========================================================
# TAB 7
# =========================================================

with tab7:

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

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption("""
Behavioral Alpha Engine © 2026  
Behavioral Finance Dashboard for RuDo Wealth
""")
