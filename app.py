import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Behavioral Alpha Engine",
    layout="wide"
)

# =========================================================
# CLEAN PROFESSIONAL CSS
# =========================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    color: #111827 !important;
}

/* MAIN BACKGROUND */

.stApp {
    background: linear-gradient(
        135deg,
        #EEF2FF,
        #E0E7FF,
        #F5F3FF
    );
}

/* REMOVE EXTRA SPACING */

.block-container {
    padding-top: 1.5rem;
    padding-bottom: 2rem;
}

/* TEXT COLORS */

p, span, div, label {
    color: #111827 !important;
}

/* HEADINGS */

h1 {
    color: #111827 !important;
    font-size: 3.6rem !important;
    font-weight: 700 !important;
}

h2, h3, h4 {
    color: #1E293B !important;
}

/* SIDEBAR */

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #E0E7FF,
        #F5F3FF
    );
    border-right: 1px solid rgba(0,0,0,0.05);
}

/* SIDEBAR TEXT */

section[data-testid="stSidebar"] * {
    color: #111827 !important;
}

/* METRIC CARDS */

[data-testid="metric-container"] {
    background: linear-gradient(
        135deg,
        #4F46E5,
        #7C3AED
    );
    border-radius: 18px;
    padding: 20px;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.12);
}

[data-testid="metric-container"] label {
    color: white !important;
}

[data-testid="metric-container"] div {
    color: white !important;
}

/* TABS */

.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
}

.stTabs [data-baseweb="tab"] {
    background: rgba(255,255,255,0.7);
    border-radius: 12px;
    color: #111827 !important;
    padding: 12px 20px;
    font-weight: 600;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(
        90deg,
        #4F46E5,
        #7C3AED
    ) !important;
    color: white !important;
}

/* INPUTS */

input, textarea {
    background-color: white !important;
    color: #111827 !important;
    border-radius: 10px !important;
}

/* SELECT BOX */

.stSelectbox div[data-baseweb="select"] {
    background-color: white !important;
    border-radius: 10px;
    border: 1px solid rgba(0,0,0,0.08);
}

/* SELECT TEXT */

.stSelectbox * {
    color: #111827 !important;
}

/* SLIDER */

.stSlider * {
    color: #111827 !important;
}

/* CUSTOM BOX */

.tech-box {
    background: rgba(255,255,255,0.75);
    border-radius: 20px;
    padding: 24px;
    backdrop-filter: blur(10px);
    box-shadow: 0px 8px 24px rgba(0,0,0,0.08);
}

/* CHAT BOX */

.chat-box {
    background: rgba(255,255,255,0.92);
    border-radius: 16px;
    padding: 22px;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
}

/* DATAFRAME */

[data-testid="stDataFrame"] {
    border-radius: 16px;
    overflow: hidden;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# DATA
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
    ]
}

df = pd.DataFrame(data)

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("Investor Profiling")

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

<h3>Behavioral Wealth Intelligence Platform</h3>

A behavioral finance and portfolio analytics system designed for RuDo Wealth to identify investor biases, understand financial behavior patterns, optimize wealth advisory, and improve long-term client outcomes.

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
    st.metric("Behavioral Score", "78/100")

with c3:
    st.metric("Portfolio Value", "₹30.7L")

with c4:
    st.metric("Risk Appetite", f"{risk_input}/10")

# =========================================================
# TABS
# =========================================================

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "Demographics",
    "Behavioral Scorecard",
    "Bias Detection",
    "Portfolio Intelligence",
    "Financial Goals",
    "AI Advisory"
])

# =========================================================
# CHART COLORS
# =========================================================

chart_colors = [
    "#4F46E5",
    "#6366F1",
    "#7C3AED",
    "#8B5CF6",
    "#A78BFA"
]

# =========================================================
# TAB 1
# =========================================================

with tab1:

    fig1 = px.histogram(
        df,
        x="Age",
        color="Investor_Type",
        title="Investor Demographics Distribution",
        color_discrete_sequence=chart_colors
    )

    fig1.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#111827"
    )

    st.plotly_chart(fig1, use_container_width=True)

# =========================================================
# TAB 2
# =========================================================

with tab2:

    st.subheader("Behavioral Bias Assessment")

    q1 = st.slider(
        "I panic when markets fall significantly",
        1,
        10,
        5
    )

    q2 = st.slider(
        "I prefer familiar investments and markets",
        1,
        10,
        5
    )

    q3 = st.slider(
        "I believe I can outperform most investors",
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
        "I check my portfolio very frequently",
        1,
        10,
        5
    )

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
            "FOMO",
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
        color="Bias",
        color_discrete_sequence=chart_colors,
        title="Behavioral Bias Breakdown"
    )

    fig2.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#111827",
        showlegend=False
    )

    st.plotly_chart(fig2, use_container_width=True)

# =========================================================
# TAB 3
# =========================================================

with tab3:

    radar = go.Figure()

    radar.add_trace(go.Scatterpolar(
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
        fill='toself',
        line_color="#4F46E5"
    ))

    radar.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="#111827",
        polar=dict(
            bgcolor="rgba(0,0,0,0)",
            radialaxis=dict(
                visible=True,
                range=[0,100]
            )
        )
    )

    st.plotly_chart(radar, use_container_width=True)

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
        color_discrete_sequence=chart_colors,
        title="Portfolio Intelligence Mapping"
    )

    fig3.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="#111827"
    )

    st.plotly_chart(fig3, use_container_width=True)

# =========================================================
# TAB 5
# =========================================================

with tab5:

    st.markdown(f"""
<div class="tech-box">

<h3>Investor Financial Profile</h3>

<b>Age:</b> {age_input} years <br><br>

<b>Annual Income:</b> ₹{income_input} LPA <br><br>

<b>Primary Goal:</b> {goal_input} <br><br>

<b>Investment Motivation:</b> {investment_reason} <br><br>

<b>Risk Appetite:</b> {risk_input}/10

</div>
""", unsafe_allow_html=True)

    allocation = px.pie(
        values=[45,25,20,10],
        names=[
            "Equity",
            "Debt",
            "Gold",
            "Cash"
        ],
        color_discrete_sequence=chart_colors,
        title="Suggested Asset Allocation"
    )

    allocation.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        font_color="#111827"
    )

    st.plotly_chart(allocation, use_container_width=True)

# =========================================================
# TAB 6
# =========================================================

with tab6:

    st.subheader("AI Wealth Advisory Assistant")

    user_question = st.text_input(
        "Ask about your investing behavior or portfolio"
    )

    if user_question:

        if overall_score > 75:

            response = """
Your behavioral profile indicates elevated emotional investing tendencies. You may benefit from disciplined SIP allocation, lower portfolio monitoring frequency, and stronger diversification strategies.
            """

        elif overall_score > 50:

            response = """
Your profile reflects moderate behavioral influence. Improving diversification and reducing trend-following behavior may improve long-term outcomes.
            """

        else:

            response = """
Your profile demonstrates relatively stable investment behavior with disciplined long-term tendencies and lower emotional volatility.
            """

        st.markdown(f"""
<div class="chat-box">

<h4>AI Advisor Response</h4>

{response}

</div>
""", unsafe_allow_html=True)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption("""
Behavioral Alpha Engine  
Behavioral Finance Research Dashboard for RuDo Wealth
""")
