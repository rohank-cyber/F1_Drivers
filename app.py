import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="F1 Driver Analytics",
    page_icon="🏎️",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

.main {
    background-color: #f4f5f7;
}

.main-title {
    font-size: 45px;
    font-weight: 800;
    text-align: center;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    margin-bottom: 30px;
}

.metric-card {
    padding: 20px;
    border-radius: 12px;
    background-color: white;
    text-align: center;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    data = pd.read_csv("F1Drivers_Dataset.csv")

    return data


df = load_data()


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="main-title">🏎️ F1 DRIVER ANALYTICS</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Formula 1 Driver Performance & Career Statistics'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.header("🔎 Dashboard Filters")


# Nationality
nationalities = sorted(df["Nationality"].dropna().unique())

selected_nationality = st.sidebar.multiselect(
    "Nationality",
    nationalities
)


# Decade
decades = sorted(df["Decade"].dropna().unique())

selected_decades = st.sidebar.multiselect(
    "Decade",
    decades
)


# Active / Retired
status = st.sidebar.selectbox(
    "Driver Status",
    ["All", "Active", "Retired"]
)


# Champion
champion_filter = st.sidebar.selectbox(
    "Championship Status",
    ["All", "Champion", "Non-Champion"]
)


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_df = df.copy()


if selected_nationality:
    filtered_df = filtered_df[
        filtered_df["Nationality"].isin(selected_nationality)
    ]


if selected_decades:
    filtered_df = filtered_df[
        filtered_df["Decade"].isin(selected_decades)
    ]


if status == "Active":
    filtered_df = filtered_df[
        filtered_df["Active"] == True
    ]

elif status == "Retired":
    filtered_df = filtered_df[
        filtered_df["Active"] == False
    ]


if champion_filter == "Champion":
    filtered_df = filtered_df[
        filtered_df["Champion"] == True
    ]

elif champion_filter == "Non-Champion":
    filtered_df = filtered_df[
        filtered_df["Champion"] == False
    ]


# ============================================================
# KPI SECTION
# ============================================================

col1, col2, col3, col4, col5 = st.columns(5)


with col1:
    st.metric(
        "👤 Drivers",
        f"{len(filtered_df):,}"
    )


with col2:
    st.metric(
        "🏆 Championships",
        f"{filtered_df['Championships'].sum():,.0f}"
    )


with col3:
    st.metric(
        "🥇 Race Wins",
        f"{filtered_df['Race_Wins'].sum():,.0f}"
    )


with col4:
    st.metric(
        "🏅 Podiums",
        f"{filtered_df['Podiums'].sum():,.0f}"
    )


with col5:
    st.metric(
        "⭐ Points",
        f"{filtered_df['Points'].sum():,.0f}"
    )


st.divider()


# ============================================================
# ROW 1
# ============================================================

col1, col2 = st.columns(2)


# ------------------------------------------------------------
# TOP CHAMPIONS
# ------------------------------------------------------------

with col1:

    top_champions = (
        filtered_df
        .nlargest(10, "Championships")
        .sort_values("Championships")
    )

    fig = px.bar(
        top_champions,
        x="Championships",
        y="Driver",
        orientation="h",
        title="🏆 Top 10 Drivers by Championships",
        hover_data=[
            "Race_Wins",
            "Podiums",
            "Points"
        ]
    )

    fig.update_layout(
        height=500,
        xaxis_title="Championships",
        yaxis_title=""
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ------------------------------------------------------------
# TOP WINNERS
# ------------------------------------------------------------

with col2:

    top_winners = (
        filtered_df
        .nlargest(10, "Race_Wins")
        .sort_values("Race_Wins")
    )

    fig = px.bar(
        top_winners,
        x="Race_Wins",
        y="Driver",
        orientation="h",
        title="🥇 Top 10 Drivers by Race Wins",
        hover_data=[
            "Championships",
            "Podiums",
            "Points"
        ]
    )

    fig.update_layout(
        height=500,
        xaxis_title="Race Wins",
        yaxis_title=""
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# ROW 2
# ============================================================

col1, col2 = st.columns(2)


# ------------------------------------------------------------
# WINS VS POINTS
# ------------------------------------------------------------

with col1:

    fig = px.scatter(
        filtered_df,
        x="Race_Wins",
        y="Points",
        size="Podiums",
        hover_name="Driver",
        hover_data=[
            "Championships",
            "Race_Entries",
            "Nationality"
        ],
        title="📈 Race Wins vs Career Points"
    )

    fig.update_layout(
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ------------------------------------------------------------
# DRIVERS BY DECADE
# ------------------------------------------------------------

with col2:

    decade_count = (
        filtered_df
        .groupby("Decade")
        .size()
        .reset_index(name="Drivers")
    )

    fig = px.line(
        decade_count,
        x="Decade",
        y="Drivers",
        markers=True,
        title="📅 Drivers by Decade"
    )

    fig.update_layout(
        height=500
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ============================================================
# NATIONALITY ANALYSIS
# ============================================================

st.subheader("🌍 Drivers by Nationality")

nationality_count = (
    filtered_df
    .groupby("Nationality")
    .size()
    .reset_index(name="Drivers")
    .sort_values("Drivers", ascending=False)
    .head(15)
)

fig = px.bar(
    nationality_count,
    x="Nationality",
    y="Drivers",
    title="Top 15 Nationalities"
)

fig.update_layout(
    xaxis_tickangle=-45,
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# ============================================================
# DRIVER COMPARISON
# ============================================================

st.divider()

st.subheader("⚔️ Driver Comparison")


drivers = sorted(df["Driver"].unique())


col1, col2 = st.columns(2)


with col1:

    driver_1 = st.selectbox(
        "Select Driver 1",
        drivers,
        index=0
    )


with col2:

    driver_2 = st.selectbox(
        "Select Driver 2",
        drivers,
        index=min(1, len(drivers)-1)
    )


d1 = df[df["Driver"] == driver_1].iloc[0]
d2 = df[df["Driver"] == driver_2].iloc[0]


comparison = pd.DataFrame({

    "Metric": [
        "Championships",
        "Race Entries",
        "Race Starts",
        "Pole Positions",
        "Race Wins",
        "Podiums",
        "Fastest Laps",
        "Points",
        "Win Rate",
        "Podium Rate"
    ],

    driver_1: [
        d1["Championships"],
        d1["Race_Entries"],
        d1["Race_Starts"],
        d1["Pole_Positions"],
        d1["Race_Wins"],
        d1["Podiums"],
        d1["Fastest_Laps"],
        d1["Points"],
        d1["Win_Rate"],
        d1["Podium_Rate"]
    ],

    driver_2: [
        d2["Championships"],
        d2["Race_Entries"],
        d2["Race_Starts"],
        d2["Pole_Positions"],
        d2["Race_Wins"],
        d2["Podiums"],
        d2["Fastest_Laps"],
        d2["Points"],
        d2["Win_Rate"],
        d2["Podium_Rate"]
    ]
})


st.dataframe(
    comparison,
    use_container_width=True,
    hide_index=True
)


# ============================================================
# DRIVER PROFILE
# ============================================================

st.divider()

st.subheader("👤 Driver Profile")


selected_driver = st.selectbox(
    "Choose a driver",
    drivers,
    key="profile_driver"
)


driver = df[df["Driver"] == selected_driver].iloc[0]


col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "Championships",
        int(driver["Championships"])
    )


with col2:
    st.metric(
        "Race Wins",
        int(driver["Race_Wins"])
    )


with col3:
    st.metric(
        "Podiums",
        int(driver["Podiums"])
    )


with col4:
    st.metric(
        "Points",
        round(driver["Points"], 1)
    )


st.write(
    f"**Nationality:** {driver['Nationality']}"
)

st.write(
    f"**Seasons:** {driver['Seasons']}"
)

st.write(
    f"**Years Active:** {driver['Years_Active']}"
)


# ============================================================
# DRIVER PERFORMANCE BAR CHART
# ============================================================

metrics = [
    "Pole_Positions",
    "Race_Wins",
    "Podiums",
    "Fastest_Laps"
]

values = [
    driver["Pole_Positions"],
    driver["Race_Wins"],
    driver["Podiums"],
    driver["Fastest_Laps"]
]


fig = px.bar(
    x=metrics,
    y=values,
    title=f"{selected_driver} - Career Performance"
)

fig.update_layout(
    xaxis_title="Performance Metric",
    yaxis_title="Count"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


# ============================================================
# FILTERED DATA
# ============================================================

with st.expander("📋 View Driver Dataset"):

    st.dataframe(
        filtered_df,
        use_container_width=True,
        hide_index=True
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.caption(
    "🏎️ F1 Driver Analytics Dashboard | "
    "Built with Python, Pandas, Plotly & Streamlit"
)