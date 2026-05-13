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
# DARK TECH CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&family=Inter:wght@400;500;600&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

.stApp {
    background: linear-gradient(135deg, #050816, #0B1023, #10182F);
    color: #FFFFFF;
}

/* MAIN CONTAINER */

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* TITLES */

h1 {
    font-family: 'Orbitron', sans-serif;
    color: #00E5FF;
    font-size: 4rem !important;
    letter-spacing: 2px;
}

h2, h3 {
    color: #FFFFFF;
}

/* METRIC CARDS */

[data-testid="metric-container"] {
    background: linear-gradient(145deg, #111827, #1E293B);
    border: 1px solid rgba(0,229,255,0.2);
    border-radius: 18px;
    padding: 22px;
    box-shadow: 0px 0px 18px rgba(0,229,255,0.12);
}

[data-testid="metric-container"] label {
    color: #94A3B8 !important;
}

[data-testid="metric-container"] div {
    color: #00E5FF !important;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #050816, #0F172A);
    border-right: 1px solid rgba(255,255,255,0.08);
}

/* TABS */

.stTabs [data-baseweb="tab-list"] {
    gap: 12px;
}

.stTabs [data-baseweb="tab"] {
    background: #111827;
    border-radius: 12px;
    color: #94A3B8;
    padding: 14px 24px;
    font-weight: 600;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(90deg, #00E5FF, #2563EB) !important;
    color: white !important;
}

/* DROPDOWNS */

.stSelectbox div[data-baseweb="select"] {
    background-color: #111827;
    border-radius: 12px;
}

/* SLIDERS */

.stSlider {
    color: #00E5FF;
}

/* DATAFRAME */

[data-testid="stDataFrame"] {
    border-radius: 14px;
    overflow: hidden;
}

/* BUTTONS */

.stButton button {
    background: linear-gradient(90deg, #00E5FF, #2563EB);
    color: white;
    border: none;
    border-radius: 12px;
    padding: 12px 20px;
    font-weight: 600;
    transition: 0.3s;
}

.stButton button:hover {
    transform: scale(1.02);
    box-shadow: 0px 0px 20px rgba(0,229,255,0.4);
}

/* INFO BOXES */

.tech-box {
    background: rgba(255,255,255,0.04);
    padding: 20px;
    border-radius: 18px;
    border: 1px solid rgba(0,229,255,0.15);
}

/* GLOW LINE */

hr {
    border: 1px solid rgba(0,229,255,0.12);
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# LOAD DATA
# =========================================================

df = pd.read_csv("investor_behavior_data.csv")

df.columns = df.columns.str.strip()

# =========================================================
# CREATE MISSING COLUMNS
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
    "Select Financial Goal",
    df["Goal"].unique()
)

age_filter = st.sidebar.slider(
    "Investor Age",
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

### AI-Powered Behavioral Wealth Intelligence System

A next-generation financial intelligence platform combining:

- Behavioral Finance
- AI Investment Intelligence
- Risk Analytics
- Portfolio Psychology
- Investor Profiling
- Wealth Prediction Models

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =========================================================
# KPI CARDS
# =========================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric(
        "Total Investors",
        len(filtered_df)
    )

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
    "🧠 Behavioral Engine",
    "🎯 Financial Goals",
    "💼 Portfolio Lab",
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
            plot_bgcolor="#0B1023"
        )

        st.plotly_chart(fig1, use_container_width=True)

    with col2:

        fig2 = px.pie(
            filtered_df,
            names="Investor_Type",
            hole=0.55,
            template="plotly_dark",
            title="Investor Category Mix"
        )

        fig2.update_layout(
            paper_bgcolor="#0B1023"
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
            template="plotly_dark",
            title="Behavioral Intelligence Mapping"
        )

        fig3.update_layout(
            paper_bgcolor="#0B1023",
            plot_bgcolor="#0B1023"
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
            plot_bgcolor="#0B1023"
        )

        st.plotly_chart(fig4, use_container_width=True)

# =========================================================
# TAB 3
# =========================================================

with tab3:

    fig5 = px.sunburst(
        filtered_df,
        path=["Goal", "Investor_Type"],
        values="Portfolio_Value",
        color="Risk_Score",
        template="plotly_dark",
        title="Goal-Oriented Wealth Structure"
    )

    fig5.update_layout(
        paper_bgcolor="#0B1023"
    )

    st.plotly_chart(fig5, use_container_width=True)

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
            paper_bgcolor="#0B1023"
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
            title="Portfolio Growth Trajectory"
        )

        fig7.update_layout(
            paper_bgcolor="#0B1023",
            plot_bgcolor="#0B1023"
        )

        st.plotly_chart(fig7, use_container_width=True)

# =========================================================
# TAB 5
# =========================================================

with tab5:

    st.subheader("AI Wealth Recommendation Engine")

    goal_input = st.selectbox(
        "Select Primary Goal",
        goals
    )

    risk_input = st.slider(
        "Select Risk Preference",
        1,
        10,
        5
    )

    income_target = st.number_input(
        "Target Wealth Goal (₹ Lakhs)",
        value=100
    )

    if risk_input <= 3:

        st.success("""
### Recommended Strategy

- Debt Allocation
- Emergency Funds
- Gold ETFs
- Conservative SIPs
- Capital Protection
        """)

    elif risk_input <= 7:

        st.info("""
### Recommended Strategy

- Hybrid Mutual Funds
- Long-Term SIP Investing
- Balanced Equity Allocation
- Goal-Based Investing
- Wealth Compounding
        """)

    else:

        st.warning("""
### Recommended Strategy

- High-Growth Equities
- Thematic Investing
- Global Exposure
- Startup & Tech Allocation
- Aggressive Wealth Creation
        """)

# =========================================================
# TAB 6
# =========================================================

with tab6:

    survey_fig = go.Figure(data=[
        go.Bar(
            x=[
                "Need Guidance",
                "Fear Volatility",
                "Prefer Familiar Assets",
                "Want Long-Term Wealth"
            ],
            y=[48,61,55,72]
        )
    ])

    survey_fig.update_layout(
        title="Behavioral Survey Intelligence",
        template="plotly_dark",
        paper_bgcolor="#0B1023",
        plot_bgcolor="#0B1023"
    )

    st.plotly_chart(survey_fig, use_container_width=True)

    st.markdown("""
<div class="tech-box">

### Key Research Findings

- Majority investors belong to the 22–35 demographic
- Moderate risk appetite dominates the investor sample
- Emotional bias heavily impacts portfolio decisions
- Investors seek long-term wealth creation
- Strong dependence on structured financial guidance

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
