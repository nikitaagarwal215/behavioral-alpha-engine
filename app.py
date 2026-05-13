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
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
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
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(
        90deg,
        #2563EB,
        #7C3AED
    ) !important;
    color: white !important;
}

/* BOX */

.tech-box {
    background: rgba(255,255,255,0.85);
    padding: 24px;
    border-radius: 20px;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.08);
}

/* CHAT BOX */

.chat-box {
    background: white;
    padding: 18px;
    border-radius: 16px;
    margin-top: 10px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# SYNTHETIC DATA
# =========================================================

data = {
    "Age": [24,28,32,35,40,45,30],
    "Income": [6,10,18,22,30,45,15],
    "Portfolio_Value": [5,12,25,35,50,70,18],
    "Risk_Score": [3,5,7,6,8,9,4],
    "Behavioral_Score": [68,72,80,76,88,92,70],
    "Investor_Type": [
        "Conservative",
        "Balanced",
        "Growth",
        "Moderate",
        "Aggressive",
        "Elite",
        "Balanced"
    ],
    "Goal": [
        "Retirement",
        "Wealth Creation",
        "Financial Freedom",
        "Passive Income",
        "Luxury Lifestyle",
        "Wealth Creation",
        "Buying Property"
    ]
}

df = pd.DataFrame(data)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("⚡ Investor Profiling")

age_input = st.sidebar.slider(
    "Age",
    18,
    60,
    28
)

income_input = st.sidebar.slider(
    "Annual Income (LPA)",
    1,
    100,
    15
)

goal_input = st.sidebar.selectbox(
    "Financial Goal",
    [
        "Retirement",
        "Wealth Creation",
        "Passive Income",
        "Buying Property",
        "Financial Freedom",
        "Children Education",
        "Luxury Lifestyle"
    ]
)

investment_reason = st.sidebar.selectbox(
    "Why Are You Investing?",
    [
        "Long-Term Wealth",
        "Financial Security",
        "Passive Income",
        "Family Future",
        "Early Retirement",
        "Lifestyle Upgrade"
    ]
)

risk_input = st.sidebar.slider(
    "Risk Appetite",
    1,
    10,
    5
)

# =========================================================
# HEADER
# =========================================================

st.title("Behavioral Alpha Engine")

st.markdown("""
<div class="tech-box">

<h3>AI-Powered Behavioral Wealth Intelligence Platform</h3>

This platform helps RuDo Wealth analyze behavioral finance patterns,
investor psychology, portfolio suitability,
and emotional investment decisions.

</div>
""", unsafe_allow_html=True)

st.markdown("---")

# =========================================================
# KPI SECTION
# =========================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("Total Investors", len(df))

with c2:
    st.metric(
        "Avg Behavioral Score",
        round(df["Behavioral_Score"].mean(),1)
    )

with c3:
    st.metric(
        "Avg Portfolio",
        f"₹{round(df['Portfolio_Value'].mean(),1)}L"
    )

with c4:
    st.metric(
        "Avg Risk Score",
        round(df["Risk_Score"].mean(),1)
    )

# =========================================================
# TABS
# =========================================================

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs([
    "📊 Demographics",
    "🧠 Behavioral Scorecard",
    "⚖ Bias Detection",
    "💼 Portfolio Intelligence",
    "🎯 Financial Goals",
    "🤖 AI Chatbot",
    "📈 Survey Insights"
])

# =========================================================
# TAB 1
# =========================================================

with tab1:

    fig1 = px.histogram(
        df,
        x="Age",
        color="Investor_Type",
        title="Investor Demographics",
        template="plotly_white"
    )

    st.plotly_chart(fig1, use_container_width=True)

# =========================================================
# TAB 2
# =========================================================

with tab2:

    st.subheader("Behavioral Bias Scorecard")

    q1 = st.slider(
        "I panic when markets fall significantly",
        1,
        10,
        5
    )

    q2 = st.slider(
        "I prefer investing in familiar assets",
        1,
        10,
        5
    )

    q3 = st.slider(
        "I believe I can beat the market consistently",
        1,
        10,
        5
    )

    q4 = st.slider(
        "I invest after seeing others make profits",
        1,
        10,
        5
    )

    q5 = st.slider(
        "I check my portfolio frequently",
        1,
        10,
        5
    )

    # SCORES

    loss_aversion = q1 * 10
    home_bias = q2 * 10
    overconfidence = q3 * 10
    fomo_bias = q4 * 10
    frequency_bias = q5 * 10

    overall_score = round(
        (
            loss_aversion +
            home_bias +
            overconfidence +
            fomo_bias +
            frequency_bias
        ) / 5,
        1
    )

    st.metric(
        "Overall Behavioral Score",
        f"{overall_score}/100"
    )

    bias_df = pd.DataFrame({
        "Bias": [
            "Loss Aversion",
            "Home Bias",
            "Overconfidence",
            "FOMO Bias",
            "Frequency Bias"
        ],
        "Score": [
            loss_aversion,
            home_bias,
            overconfidence,
            fomo_bias,
            frequency_bias
        ]
    })

    fig2 = px.bar(
        bias_df,
        x="Bias",
        y="Score",
        color="Score",
        template="plotly_white",
        title="Behavioral Bias Breakdown"
    )

    st.plotly_chart(fig2, use_container_width=True)

# =========================================================
# TAB 3
# =========================================================

with tab3:

    radar_fig = go.Figure()

    radar_fig.add_trace(go.Scatterpolar(
        r=[
            loss_aversion,
            home_bias,
            overconfidence,
            fomo_bias,
            frequency_bias
        ],
        theta=[
            "Loss Aversion",
            "Home Bias",
            "Overconfidence",
            "FOMO",
            "Frequency Bias"
        ],
        fill='toself'
    ))

    radar_fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0,100]
            )
        ),
        showlegend=False,
        template="plotly_white"
    )

    st.plotly_chart(radar_fig, use_container_width=True)

# =========================================================
# TAB 4
# =========================================================

with tab4:

    fig3 = px.scatter(
        df,
        x="Risk_Score",
        y="Portfolio_Value",
        size="Behavioral_Score",
        color="Investor_Type",
        title="Portfolio Intelligence Mapping",
        template="plotly_white"
    )

    st.plotly_chart(fig3, use_container_width=True)

# =========================================================
# TAB 5
# =========================================================

with tab5:

    st.subheader("Financial Goal Intelligence")

    st.markdown(f"""
<div class="tech-box">

<h3>Investor Summary</h3>

<b>Age:</b> {age_input} years <br>
<b>Annual Income:</b> ₹{income_input} LPA <br>
<b>Primary Goal:</b> {goal_input} <br>
<b>Investment Motivation:</b> {investment_reason} <br>
<b>Risk Appetite:</b> {risk_input}/10

</div>
""", unsafe_allow_html=True)

    goal_chart = px.pie(
        values=[40,30,20,10],
        names=[
            "Equity",
            "Debt",
            "Gold",
            "Cash"
        ],
        title="Suggested Asset Allocation",
        template="plotly_white"
    )

    st.plotly_chart(goal_chart, use_container_width=True)

# =========================================================
# TAB 6
# =========================================================

with tab6:

    st.subheader("AI Financial Chatbot")

    user_question = st.text_input(
        "Ask the AI anything about your investment behavior"
    )

    if user_question:

        if overall_score > 75:

            response = """
You show high behavioral influence in your investing decisions.
You may benefit from structured long-term investing
and reduced emotional trading activity.
            """

        elif overall_score > 50:

            response = """
Your investing behavior appears moderately balanced.
You should focus on improving diversification
and maintaining disciplined investing habits.
            """

        else:

            response = """
Your investing behavior appears relatively stable.
You demonstrate disciplined investing tendencies
with lower emotional influence.
            """

        st.markdown(f"""
<div class="chat-box">

<h4>AI Advisor Response</h4>

{response}

</div>
""", unsafe_allow_html=True)

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

    st.markdown("""
<div class="tech-box">

<h3>Key Research Findings</h3>

Most investors belong to the 22–35 demographic
and display moderate-to-high behavioral influence
in financial decision-making.

Long-term wealth creation remains the dominant financial objective.

</div>
""", unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption("""
Behavioral Alpha Engine © 2026  
Behavioral Finance Dashboard for RuDo Wealth
""")
