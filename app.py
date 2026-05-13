import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Behavioral Alpha Engine",
    page_icon="💎",
    layout="wide"
)

# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

.main {
    background-color: #F4F9FF;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

h1, h2, h3 {
    color: #0A2540;
    font-family: 'Segoe UI';
}

[data-testid="metric-container"] {
    background: linear-gradient(135deg, #0A66C2, #4DA8FF);
    padding: 20px;
    border-radius: 18px;
    color: white;
    box-shadow: 0px 4px 18px rgba(0,0,0,0.08);
}

[data-testid="metric-container"] label {
    color: white !important;
}

.stTabs [data-baseweb="tab-list"] {
    gap: 10px;
}

.stTabs [data-baseweb="tab"] {
    background-color: #EAF4FF;
    border-radius: 12px;
    padding: 12px 20px;
    color: #0A2540;
    font-weight: 600;
}

.stTabs [aria-selected="true"] {
    background-color: #0A66C2 !important;
    color: white !important;
}

.sidebar .sidebar-content {
    background-color: #FFFFFF;
}

div.stButton > button {
    background-color: #0A66C2;
    color: white;
    border-radius: 12px;
    border: none;
    padding: 10px 20px;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

# =========================================================
# LOAD DATA
# =========================================================

df = pd.read_csv("investor_behavior_data.csv")

df.columns = df.columns.str.strip()

# =========================================================
# SYNTHETIC DATA CREATION
# =========================================================

if "Age" not in df.columns:
    df["Age"] = [23,25,27,30,34,38,42] * (len(df)//7) + [25]*(len(df)%7)

if "Income" not in df.columns:
    df["Income"] = [6,8,12,15,20,30,45] * (len(df)//7) + [10]*(len(df)%7)

if "Behavioral_Score" not in df.columns:
    df["Behavioral_Score"] = [65,70,78,84,58,92,76] * (len(df)//7) + [70]*(len(df)%7)

if "Risk_Score" not in df.columns:
    df["Risk_Score"] = [2,3,5,6,8,9,4] * (len(df)//7) + [5]*(len(df)%7)

if "Portfolio_Value" not in df.columns:
    df["Portfolio_Value"] = [4,7,10,18,30,45,60] * (len(df)//7) + [8]*(len(df)%7)

if "Investor_Type" not in df.columns:
    df["Investor_Type"] = [
        "Conservative",
        "Balanced",
        "Growth",
        "Aggressive",
        "Moderate",
        "Elite",
        "Passive"
    ] * (len(df)//7) + ["Balanced"]*(len(df)%7)

# =========================================================
# NEW GOALS COLUMN
# =========================================================

goals = [
    "Retirement",
    "Wealth Creation",
    "Passive Income",
    "Buying a House",
    "Early Financial Freedom",
    "Luxury Lifestyle",
    "Children Education"
]

df["Goal"] = [goals[i % len(goals)] for i in range(len(df))]

# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.title("⚡ Behavioral Alpha Engine")

selected_goal = st.sidebar.selectbox(
    "Select Financial Goal",
    df["Goal"].unique()
)

selected_age = st.sidebar.slider(
    "Age Range",
    int(df["Age"].min()),
    int(df["Age"].max()),
    (22,45)
)

selected_income = st.sidebar.slider(
    "Current Income (LPA)",
    int(df["Income"].min()),
    int(df["Income"].max()),
    (5,45)
)

selected_risk = st.sidebar.slider(
    "Risk Appetite",
    1,
    10,
    (2,9)
)

filtered_df = df[
    (df["Goal"] == selected_goal) &
    (df["Age"] >= selected_age[0]) &
    (df["Age"] <= selected_age[1]) &
    (df["Income"] >= selected_income[0]) &
    (df["Income"] <= selected_income[1]) &
    (df["Risk_Score"] >= selected_risk[0]) &
    (df["Risk_Score"] <= selected_risk[1])
]

# =========================================================
# HEADER
# =========================================================

st.title("💎 Behavioral Alpha Engine")

st.subheader("AI-Powered Behavioral Wealth Intelligence Platform")

st.markdown("""
An advanced behavioral finance dashboard analyzing:

- Investor psychology  
- Wealth goals  
- Risk appetite  
- Financial behavior  
- Portfolio intelligence  
- AI-driven investment insights  
""")

# =========================================================
# METRICS
# =========================================================

st.markdown("---")

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
    "📈 AI Insights",
    "📋 Survey Analytics"
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
            title="Investor Category Split",
            hole=0.45,
            template="plotly_white"
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
            title="Behavioral vs Risk Mapping",
            template="plotly_white"
        )

        st.plotly_chart(fig3, use_container_width=True)

    with col2:

        fig4 = px.bar(
            filtered_df,
            x="Investor_Type",
            y="Behavioral_Score",
            color="Investor_Type",
            title="Behavioral Score by Investor Type",
            template="plotly_white"
        )

        st.plotly_chart(fig4, use_container_width=True)

# =========================================================
# TAB 3
# =========================================================

with tab3:

    st.markdown("## Financial Goal Intelligence")

    goal_chart = px.sunburst(
        filtered_df,
        path=["Goal", "Investor_Type"],
        values="Portfolio_Value",
        color="Risk_Score",
        template="plotly_white"
    )

    st.plotly_chart(goal_chart, use_container_width=True)

    st.dataframe(filtered_df[[
        "Age",
        "Income",
        "Goal",
        "Investor_Type",
        "Behavioral_Score"
    ]])

# =========================================================
# TAB 4
# =========================================================

with tab4:

    col1, col2 = st.columns(2)

    with col1:

        fig5 = px.treemap(
            filtered_df,
            path=["Investor_Type"],
            values="Portfolio_Value",
            color="Behavioral_Score",
            template="plotly_white",
            title="Portfolio Allocation"
        )

        st.plotly_chart(fig5, use_container_width=True)

    with col2:

        fig6 = px.line(
            filtered_df.sort_values("Age"),
            x="Age",
            y="Portfolio_Value",
            color="Investor_Type",
            template="plotly_white",
            title="Portfolio Growth Curve"
        )

        st.plotly_chart(fig6, use_container_width=True)

# =========================================================
# TAB 5
# =========================================================

with tab5:

    st.markdown("## AI Investment Recommendation Engine")

    investor_goal = st.selectbox(
        "Select Your Primary Goal",
        goals
    )

    risk_level = st.slider(
        "Select Risk Appetite",
        1,
        10,
        5
    )

    if risk_level <= 3:

        st.success("""
        Recommended AI Strategy:
        
        - Capital Preservation  
        - Debt Funds  
        - Gold ETFs  
        - SIP Diversification  
        - Emergency Fund Optimization  
        """)

    elif risk_level <= 7:

        st.info("""
        Recommended AI Strategy:
        
        - Balanced Mutual Funds  
        - Equity + Debt Allocation  
        - Wealth Compounding  
        - Long-Term SIPs  
        - Goal-Based Investing  
        """)

    else:

        st.warning("""
        Recommended AI Strategy:
        
        - High-Growth Equity  
        - Thematic Investing  
        - Global Diversification  
        - Startup/Tech Exposure  
        - Aggressive Wealth Creation  
        """)

# =========================================================
# TAB 6
# =========================================================

with tab6:

    survey = go.Figure(data=[
        go.Bar(
            x=[
                "Prefer Familiar Assets",
                "Need Financial Guidance",
                "Fear Market Volatility",
                "Prefer Long-Term Investing"
            ],
            y=[55,48,61,72]
        )
    ])

    survey.update_layout(
        title="Behavioral Finance Survey Findings",
        template="plotly_white"
    )

    st.plotly_chart(survey, use_container_width=True)

    st.markdown("""
    ### Key Research Insights
    
    - Most investors belong to the 22–35 age category  
    - Emotional investing significantly impacts decision-making  
    - Moderate-risk investors dominate the sample population  
    - Long-term wealth creation is the primary financial goal  
    - Investors show strong dependency on behavioral triggers  
    """)

# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.caption("""
Behavioral Alpha Engine © 2026  
AI-Driven Behavioral Finance Research Dashboard
""")
