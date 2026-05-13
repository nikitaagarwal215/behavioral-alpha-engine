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

/* BACKGROUND */

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

/* CUSTOM BOX */

.tech-box {
    background: rgba(255,255,255,0.85);
    padding: 24px;
    border-radius: 20px;
    box-shadow: 0px 8px 20px rgba(0,0,0,0.08);
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
# HEADER
# =========================================================

st.title("Behavioral Alpha Engine")

st.markdown("""
<div class="tech-box">

<h3>AI-Powered Behavioral Wealth Intelligence Dashboard</h3>

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
# MAIN TABS
# =========================================================

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 Demographics",
    "🧠 Behavioral Scorecard",
    "⚖ Bias Detection Engine",
    "💼 Portfolio Intelligence",
    "🤖 AI Advisory",
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

    # =====================================================
    # INTERACTIVE QUESTIONS
    # =====================================================

    q1 = st.slider(
        "I panic when markets fall significantly",
        1,
        10,
        5
    )

    q2 = st.slider(
        "I prefer investing in familiar markets/assets",
        1,
        10,
        5
    )

    q3 = st.slider(
        "I believe I can outperform the market consistently",
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
        "I check my investments very frequently",
        1,
        10,
        5
    )

    # =====================================================
    # CALCULATED SCORES
    # =====================================================

    loss_aversion = q1 * 10
    home_bias = q2 * 10
    overconfidence = q3 * 10
    fomo_bias = q4 * 10
    frequency_bias = q5 * 10

    total_behavior_score = round(
        (
            loss_aversion +
            home_bias +
            overconfidence +
            fomo_bias +
            frequency_bias
        ) / 5,
        1
    )

    # =====================================================
    # DISPLAY SCORE
    # =====================================================

    st.markdown("---")

    st.metric(
        "Overall Behavioral Score",
        f"{total_behavior_score}/100"
    )

    # =====================================================
    # SCORE TABLE
    # =====================================================

    score_df = pd.DataFrame({
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
        score_df,
        x="Bias",
        y="Score",
        color="Score",
        title="Behavioral Bias Breakdown",
        template="plotly_white"
    )

    st.plotly_chart(fig2, use_container_width=True)

    # =====================================================
    # INTERPRETATION
    # =====================================================

    st.markdown("""
<div class="tech-box">

<h3>Behavioral Interpretation</h3>

High loss aversion suggests emotional panic-selling tendencies during volatility.

High home bias indicates preference toward familiar or geographically concentrated assets.

High overconfidence reflects excessive trading confidence and market timing belief.

Elevated FOMO scores indicate trend-chasing and social investing behavior.

High frequency bias indicates excessive portfolio monitoring behavior.

</div>
""", unsafe_allow_html=True)

# =========================================================
# TAB 3
# =========================================================

with tab3:

    st.subheader("Bias Detection Engine")

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

    st.markdown("""
<div class="tech-box">

<h3>Portfolio Intelligence</h3>

This section helps RuDo Wealth identify
which investor categories are emotionally driven,
overexposed to risk,
or under-diversified.

</div>
""", unsafe_allow_html=True)

# =========================================================
# TAB 5
# =========================================================

with tab5:

    st.subheader("AI Recommendation Engine")

    risk_input = st.slider(
        "Select Risk Appetite",
        1,
        10,
        5
    )

    if risk_input <= 3:

        st.success("""
Recommended Strategy:

Conservative debt allocation,
gold exposure,
and capital preservation investing.
        """)

    elif risk_input <= 7:

        st.info("""
Recommended Strategy:

Balanced long-term investing strategy
with diversified SIP allocation.
        """)

    else:

        st.warning("""
Recommended Strategy:

Aggressive growth investing involving
high-growth equities and global diversification.
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
