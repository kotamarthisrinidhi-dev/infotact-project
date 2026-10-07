import pandas as pd
import streamlit as st
from pathlib import Path
from textwrap import dedent
import plotly.express as px
import plotly.graph_objects as go

# PAGE CONFIG

st.set_page_config(
    page_title="AtmoSync | Climate Intelligence",
    page_icon="🌦️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# PREMIUM UI STYLE

st.markdown(
    """
    <style>

    .stApp {
        background-color: #f4f7fb;
    }

    .block-container {
        max-width: 1500px;
        padding-top: 1.5rem;
    }

    /* HERO */
     .hero {
    background: linear-gradient(
        135deg,
        #071a2f 0%,
        #103d5c 55%,
        #147d8c 100%
    );

    padding: 30px 34px;
    border-radius: 18px;
    color: white;

    box-shadow:
        0 12px 35px rgba(15, 23, 42, 0.16);

    margin-bottom: 22px;
}

.hero-title {
    font-size: 38px;
    font-weight: 800;
    letter-spacing: -1px;
    line-height: 1.2;
}

.hero-subtitle {
    font-size: 16px;
    opacity: 0.85;
    margin-top: 8px;
}

.hero-status {
    display: inline-block;
    margin-top: 18px;
    padding: 7px 14px;
    border-radius: 20px;
    background: rgba(255,255,255,0.13);
    font-size: 12px;
    font-weight: 600;
}

    /* KPI */

    .kpi {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 18px;
        min-height: 125px;

        box-shadow:
            0 5px 18px rgba(15, 23, 42, 0.05);
    }

    .kpi-label {
        font-size: 11px;
        color: #64748b;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 0.5px;
    }

    .kpi-value {
        color: #0f2d4a;
        font-size: 28px;
        font-weight: 800;
        margin-top: 8px;
    }

    .kpi-note {
        color: #94a3b8;
        font-size: 12px;
        margin-top: 4px;
    }

    /* INSIGHTS */

    .insight {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 14px;
        padding: 18px;
        min-height: 135px;
        box-shadow:
            0 4px 15px rgba(15, 23, 42, 0.04);
    }

    .insight-label {
        font-size: 11px;
        color: #64748b;
        font-weight: 700;
        text-transform: uppercase;
    }

    .insight-title {
        font-size: 18px;
        color: #0f2d4a;
        font-weight: 750;
        margin-top: 7px;
    }

    .insight-text {
        font-size: 13px;
        color: #64748b;
        margin-top: 6px;
        line-height: 1.5;
    }

    /* SECTION */

    .section {
        font-size: 22px;
        font-weight: 750;
        color: #102f4d;
        margin-top: 20px;
        margin-bottom: 12px;
    }

    /* SIDEBAR */

    section[data-testid="stSidebar"] {
        background:
            linear-gradient(
                180deg,
                #071a2f 0%,
                #0d2944 100%
            );
    }

    section[data-testid="stSidebar"] {
        color: white;
    }

    /* Labels/headings sit directly on the dark sidebar background,
       so they stay white. */
    section[data-testid="stSidebar"] label,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] [data-testid="stMarkdownContainer"],
    section[data-testid="stSidebar"] [data-testid="stWidgetLabel"] {
        color: white;
    }

    /* The date input, selectbox and multiselect boxes render on a
       white background, so their text must stay dark or it becomes
       invisible (white text on white background). */
    section[data-testid="stSidebar"] input,
    section[data-testid="stSidebar"] [data-baseweb="input"],
    section[data-testid="stSidebar"] [data-baseweb="select"],
    section[data-testid="stSidebar"] [data-baseweb="select"] div,
    section[data-testid="stSidebar"] [data-baseweb="select"] span,
    section[data-testid="stSidebar"] [data-baseweb="popover"],
    section[data-testid="stSidebar"] [data-baseweb="calendar"] {
        color: #0f2d4a !important;
    }

    /* Multiselect tags keep white text since they sit on a
       colored (not white) chip background. */
    section[data-testid="stSidebar"] [data-baseweb="tag"],
    section[data-testid="stSidebar"] [data-baseweb="tag"] span {
        color: white !important;
    }

    /* Reset Filters button — background set explicitly so the
       text color always has contrast, in both normal and hover
       states (white text alone was invisible on a white button). */
    section[data-testid="stSidebar"] .stButton button {
        background-color: #0f2d4a;
        color: white !important;
        border: 1px solid rgba(255,255,255,0.15);
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.25);
        transition: box-shadow 0.15s ease, background-color 0.15s ease;
    }

    section[data-testid="stSidebar"] .stButton button:hover {
        background-color: #163e63;
        color: white !important;
        box-shadow: 0 8px 22px rgba(0, 0, 0, 0.35);
    }

    /* FOOTER */

    .footer {
        text-align: center;
        color: #94a3b8;
        font-size: 12px;
        padding: 30px 0;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# CONSTANTS

FILENAME = "atmosync_microclimate_cleaned.csv"
APP_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = APP_DIR.parent

# Checked in order — covers both common layouts so the app works
# regardless of whether "processed" sits under "data" or at project root.
CANDIDATE_PATHS = [
    PROJECT_ROOT / "data" / "processed" / FILENAME,
    PROJECT_ROOT / "processed" / FILENAME,
    APP_DIR / "data" / "processed" / FILENAME,
    APP_DIR / "processed" / FILENAME,
]

DATA_PATH = next((p for p in CANDIDATE_PATHS if p.exists()), CANDIDATE_PATHS[0])

REQUIRED_COLUMNS = [
    "date",
    "location",
    "temp_max_c",
    "temp_min_c",
    "rainfall_mm",
    "humidity_pct",
    "wind_speed_kmph"
]

NUMERIC_COLUMNS = [
    "temp_max_c",
    "temp_min_c",
    "rainfall_mm",
    "humidity_pct",
    "wind_speed_kmph"
]


# LOAD DATA

@st.cache_data
def load_data(path):
    return pd.read_csv(path)


if not DATA_PATH.exists():

    checked_list = "\n".join(f"- {p}" for p in CANDIDATE_PATHS)

    st.error(
        "Cleaned dataset not found.\n\n"
        f"Looked for **{FILENAME}** in these locations:\n\n"
        f"{checked_list}\n\n"
        "Place the file in one of these, or update CANDIDATE_PATHS "
        "in app.py to match your folder layout."
    )

    st.stop()


try:

    df = load_data(str(DATA_PATH))

except Exception as error:

    st.error(f"Unable to load dataset: {error}")

    st.stop()

# VALIDATE DATA

missing_columns = [
    column
    for column in REQUIRED_COLUMNS
    if column not in df.columns
]

if missing_columns:

    st.error(
        f"Missing required columns: {missing_columns}"
    )

    st.stop()


df["date"] = pd.to_datetime(
    df["date"],
    errors="coerce"
)

for column in NUMERIC_COLUMNS:

    df[column] = pd.to_numeric(
        df[column],
        errors="coerce"
    )


df = df.dropna(
    subset=["date"]
).copy()


if df.empty:

    st.error("No valid weather records available.")

    st.stop()

# SIDEBAR

with st.sidebar:

    st.html(dedent("""
        <div style="
            font-size:29px;
            font-weight:800;
        ">
            🌦️ AtmoSync
        </div>

        <div style="
            color:#9fb3c8;
            font-size:13px;
            margin-top:4px;
        ">
            Climate Intelligence Platform
        </div>
        """))

    st.divider()

    st.markdown("### Control Center")

    min_date = df["date"].min().date()
    max_date = df["date"].max().date()

    date_range = st.date_input(
        "Analysis Period",
        value=(min_date, max_date),
        min_value=min_date,
        max_value=max_date
    )

    if (
        isinstance(date_range, tuple)
        and len(date_range) == 2
    ):

        start_date = pd.Timestamp(
            date_range[0]
        )

        end_date = pd.Timestamp(
            date_range[1]
        )

    else:

        start_date = pd.Timestamp(min_date)
        end_date = pd.Timestamp(max_date)


    locations = sorted(
        df["location"]
        .dropna()
        .unique()
        .tolist()
    )

    selected_locations = st.multiselect(
        "Locations",
        locations,
        default=locations
    )


    if st.button(
        "↻ Reset Filters",
        use_container_width=True,
        width="stretch"
    ):

        st.rerun()

# FILTER

filtered_df = df[
    (df["date"] >= start_date)
    & (df["date"] <= end_date)
    & (
        df["location"].isin(
            selected_locations
        )
    )
].copy()


if filtered_df.empty:

    st.warning(
        "No records match the current filters."
    )

    st.info(
        "Select another location or date range."
    )

    st.stop()

# CALCULATIONS

record_count = len(filtered_df)

location_count = filtered_df[
    "location"
].nunique()

avg_max_temp = filtered_df[
    "temp_max_c"
].mean()

avg_min_temp = filtered_df[
    "temp_min_c"
].mean()

avg_rainfall = filtered_df[
    "rainfall_mm"
].mean()

avg_humidity = filtered_df[
    "humidity_pct"
].mean()

avg_wind = filtered_df[
    "wind_speed_kmph"
].mean()


# DATA QUALITY

quality_columns = REQUIRED_COLUMNS

total_cells = (
    len(filtered_df)
    * len(quality_columns)
)

missing_cells = filtered_df[
    quality_columns
].isna().sum().sum()

if total_cells > 0:

    completeness = (
        1 - missing_cells / total_cells
    ) * 100

else:

    completeness = 0

# HERO

hero_html = f"""
<div class="hero">

    <div class="hero-title">
        🌦️ AtmoSync
    </div>

    <div class="hero-subtitle">
        Location-Level Weather Analytics & Intelligence
    </div>

    <div class="hero-status">
        <span>● ANALYTICS MODE</span>
        &nbsp;&nbsp;|&nbsp;&nbsp;
        <span>{record_count:,} observations</span>
        &nbsp;&nbsp;|&nbsp;&nbsp;
        <span>{location_count} locations</span>
    </div>

</div>
"""

st.html(hero_html)

# MAIN NAVIGATION

page = st.radio(
    "",[
    label="Navigation Menu", # Provides a descriptive label for screen readers
    options=[
        "3️⃣ Executive Command Center",
        "4️⃣ Location Intelligence",
        "5️⃣ Climate & Data Intelligence"
    ],
    horizontal=True
    label_visibility="collapsed" # Hides the label from the visual UI
)

# EXECUTIVE COMMAND CENTER

if page == "3️⃣ Executive Command Center":

    st.markdown(
        '<div class="section">Executive Performance Snapshot</div>',
        unsafe_allow_html=True
    )


    k1, k2, k3, k4, k5 = st.columns(5)


    with k1:
        st.html(dedent(f"""
        <div class="kpi">

            <div class="kpi-label">
                Observations
            </div>

            <div class="kpi-value">
                {record_count:,}
            </div>

            <div class="kpi-note">
                Filtered records
            </div>

        </div>
    """)
)

    with k2:

        st.html(dedent(
            f"""
            <div class="kpi">

                <div class="kpi-label">
                    Locations
                </div>

                <div class="kpi-value">
                    {location_count}
                </div>

                <div class="kpi-note">
                    Active locations
                </div>

            </div>
            """)
        )


    with k3:

        st.html(dedent(
            f"""
            <div class="kpi">

                <div class="kpi-label">
                    Avg Max Temp
                </div>

                <div class="kpi-value">
                    {avg_max_temp:.1f} °C
                </div>

                <div class="kpi-note">
                    Average maximum
                </div>

            </div>
            """)
        )


    with k4:

        st.html(
            dedent(f"""
            <div class="kpi">

                <div class="kpi-label">
                    Avg Rainfall
                </div>

                <div class="kpi-value">
                    {avg_rainfall:.1f} mm
                </div>

                <div class="kpi-note">
                    Average rainfall
                </div>

            </div>
            """)
     
        )


    with k5:

        st.html(dedent(
            f"""
            <div class="kpi">

                <div class="kpi-label">
                    Avg Humidity
                </div>

                <div class="kpi-value">
                    {avg_humidity:.1f}%
                </div>

                <div class="kpi-note">
                    Relative humidity
                </div>

            </div>
            """)
        )

    # AUTOMATED INSIGHTS
    
    st.markdown(
        '<div class="section">Executive Intelligence</div>',
        unsafe_allow_html=True
    )


    location_stats = (
        filtered_df
        .groupby("location")
        .agg(
            avg_temp=("temp_max_c", "mean"),
            rainfall=("rainfall_mm", "mean"),
            humidity=("humidity_pct", "mean"),
            wind=("wind_speed_kmph", "mean"),
            variability=("temp_max_c", "std")
        )
        .reset_index()
    )


    hottest = location_stats.loc[
        location_stats["avg_temp"].idxmax()
    ]

    wettest = location_stats.loc[
        location_stats["rainfall"].idxmax()
    ]

    most_humid = location_stats.loc[
        location_stats["humidity"].idxmax()
    ]

    temp_location = hottest["location"]
    max_temp = hottest["avg_temp"]

    rain_location = wettest["location"]
    max_rainfall = wettest["rainfall"]

    humidity_location = most_humid["location"]
    max_humidity = most_humid["humidity"]


    st.html(dedent("""
        <style>
        .insight-card {
            background: rgba(255,255,255,0.75);
            border: 1px solid rgba(0,0,0,0.06);
            border-radius: 18px;
            padding: 24px;
            min-height: 190px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.04);
        }

        .insight-label {
            font-size: 13px;
            font-weight: 600;
            color: #64748b;
            text-transform: uppercase;
            letter-spacing: 0.08em;
            margin-bottom: 12px;
        }

        .insight-title {
            font-size: 22px;
            font-weight: 700;
            color: #111827;
            margin-bottom: 18px;
        }

        .insight-text {
            font-size: 15px;
            line-height: 1.6;
            color: #475569;
        }

        .insight-text b {
            color: #111827;
        }
        </style>
        """))

    col1, col2, col3 = st.columns(3)

    with col1:
        st.html(dedent(f"""
            <div class="insight-card">
                <div class="insight-label">
                    Temperature Leader
                </div>

                <div class="insight-title">
                    🌡️ {temp_location}
                </div>

                <div class="insight-text">
                    Highest average maximum temperature:
                    <b>{max_temp:.2f} °C</b>.
                </div>
            </div>
            """))

    with col2:
        st.html(dedent(f"""
            <div class="insight-card">
                <div class="insight-label">
                    Rainfall Signal
                </div>

                <div class="insight-title">
                    🌧️ {rain_location}
                </div>

                <div class="insight-text">
                    Highest average rainfall:
                    <b>{max_rainfall:.2f} mm</b>.
                </div>
            </div>
            """))

    with col3:
        st.html(dedent(f"""
            <div class="insight-card">
                <div class="insight-label">
                    Humidity Signal
                </div>

                <div class="insight-title">
                    💧 {humidity_location}
                </div>

                <div class="insight-text">
                    Highest average humidity:
                    <b>{max_humidity:.2f}%</b>.
                </div>
            </div>
            """))

    # MAIN TREND

    st.markdown(
        '<div class="section">Temperature Intelligence</div>',
        unsafe_allow_html=True
    )


    daily = (
        filtered_df
        .groupby("date")[
            [
                "temp_max_c",
                "temp_min_c"
            ]
        ]
        .mean()
        .reset_index()
    )


    fig = go.Figure()

    fig.add_trace(
        go.Scatter(
            x=daily["date"],
            y=daily["temp_max_c"],
            mode="lines",
            name="Maximum Temperature",
            line=dict(width=3)
        )
    )

    fig.add_trace(
        go.Scatter(
            x=daily["date"],
            y=daily["temp_min_c"],
            mode="lines",
            name="Minimum Temperature",
            line=dict(width=3)
        )
    )

    fig.update_layout(
        height=450,
        template="plotly_white",
        hovermode="x unified",
        title="Daily Temperature Movement",
        xaxis_title="Date",
        yaxis_title="Temperature (°C)"
    )

    st.plotly_chart(
        fig,
        use_container_width=True,
        width="stretch"

    )

    # LOCATION SNAPSHOT
   
    st.markdown(
        '<div class="section">Location Performance Snapshot</div>',
        unsafe_allow_html=True
    )


    summary = (
        filtered_df
        .groupby("location")
        .agg(
            Records=("location", "size"),
            Avg_Max_Temp=("temp_max_c", "mean"),
            Avg_Min_Temp=("temp_min_c", "mean"),
            Avg_Rainfall=("rainfall_mm", "mean"),
            Avg_Humidity=("humidity_pct", "mean"),
            Avg_Wind=("wind_speed_kmph", "mean")
        )
        .reset_index()
        .round(2)
    )


    st.dataframe(
        summary,
        use_container_width=True,
        width="stretch",
        hide_index=True
    )

# LOCATION INTELLIGENCE

if page == "4️⃣ Location Intelligence":

    st.markdown(
        '<div class="section">Location Intelligence</div>',
        unsafe_allow_html=True
    )

    # TEMPERATURE COMPARISON

    temp_location = (
        filtered_df
        .groupby("location")[
            [
                "temp_max_c",
                "temp_min_c"
            ]
        ]
        .mean()
        .reset_index()
    )

    temp_long = temp_location.melt(
        id_vars="location",
        var_name="Metric",
        value_name="Temperature"
    )

    temp_long["Metric"] = temp_long[
        "Metric"
    ].replace(
        {
            "temp_max_c": "Average Maximum",
            "temp_min_c": "Average Minimum"
        }
    )

    fig_temp = px.bar(
        temp_long,
        x="location",
        y="Temperature",
        color="Metric",
        barmode="group",
        title="Temperature Comparison by Location",
        labels={
            "location": "Location",
            "Temperature": "Temperature (°C)"
        }
    )

    fig_temp.update_layout(
        template="plotly_white",
        height=430
    )

    st.plotly_chart(
        fig_temp,
        use_container_width=True
       width="stretch"
    )

    # THREE WEATHER METRICS


    c1, c2, c3 = st.columns(3)


    with c1:

        rainfall = (
            filtered_df
            .groupby("location")[
                "rainfall_mm"
            ]
            .mean()
            .reset_index()
        )


        fig = px.bar(
            rainfall,
            x="location",
            y="rainfall_mm",
            title="Average Rainfall",
            labels={
                "rainfall_mm": "Rainfall (mm)"
            }
        )

        fig.update_layout(
            template="plotly_white",
            height=350
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            width="stretch"

        )


    with c2:

        humidity = (
            filtered_df
            .groupby("location")[
                "humidity_pct"
            ]
            .mean()
            .reset_index()
        )


        fig = px.bar(
            humidity,
            x="location",
            y="humidity_pct",
            title="Average Humidity",
            labels={
                "humidity_pct": "Humidity (%)"
            }
        )

        fig.update_layout(
            template="plotly_white",
            height=350
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            width="stretch"
        )


    with c3:

        wind = (
            filtered_df
            .groupby("location")[
                "wind_speed_kmph"
            ]
            .mean()
            .reset_index()
        )


        fig = px.bar(
            wind,
            x="location",
            y="wind_speed_kmph",
            title="Average Wind Speed",
            labels={
                "wind_speed_kmph": "Wind (km/h)"
            }
        )

        fig.update_layout(
            template="plotly_white",
            height=350
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            width="stretch"

        )

    # LOCATION PROFILE

    st.markdown(
        '<div class="section">Location Profile</div>',
        unsafe_allow_html=True
    )


    selected_profile = st.selectbox(
        "Choose location",
        sorted(
            filtered_df["location"]
            .dropna()
            .unique()
        )
    )


    profile = filtered_df[
        filtered_df["location"]
        == selected_profile
    ]


    p1, p2, p3, p4 = st.columns(4)


    with p1:

        st.metric(
            "Max Temperature",
            f"{profile['temp_max_c'].mean():.2f} °C"
        )


    with p2:

        st.metric(
            "Rainfall",
            f"{profile['rainfall_mm'].mean():.2f} mm"
        )


    with p3:

        st.metric(
            "Humidity",
            f"{profile['humidity_pct'].mean():.2f}%"
        )


    with p4:

        st.metric(
            "Wind",
            f"{profile['wind_speed_kmph'].mean():.2f} km/h"
        )

    # SCATTER
   
    st.markdown(
        '<div class="section">Climate Relationship Map</div>',
        unsafe_allow_html=True
    )

    scatter_axis_labels = {
        "Maximum Temperature (°C)": "temp_max_c",
        "Minimum Temperature (°C)": "temp_min_c",
        "Rainfall (mm)": "rainfall_mm",
        "Humidity (%)": "humidity_pct",
        "Wind Speed (km/h)": "wind_speed_kmph",
    }

    axis_col1, axis_col2 = st.columns(2)

    with axis_col1:
        x_axis_label = st.selectbox(
            "X-axis",
            list(scatter_axis_labels.keys()),
            index=0,
            key="scatter_x_axis"
        )

    with axis_col2:
        y_axis_label = st.selectbox(
            "Y-axis",
            list(scatter_axis_labels.keys()),
            index=3,
            key="scatter_y_axis"
        )

    x_axis_col = scatter_axis_labels[x_axis_label]
    y_axis_col = scatter_axis_labels[y_axis_label]

    # Bubble size uses rainfall by default, unless rainfall is
    # already one of the chosen axes — then fall back to wind speed
    # so the size channel still adds information instead of repeating
    # an axis.
    size_col = "rainfall_mm"
    if size_col in (x_axis_col, y_axis_col):
        size_col = "wind_speed_kmph"

    fig = px.scatter(
        filtered_df,
        x=x_axis_col,
        y=y_axis_col,
        color="location",
        size=size_col,
        hover_data=[
            "date",
            "wind_speed_kmph"
        ],
        title=f"{x_axis_label.split(' (')[0]} vs {y_axis_label.split(' (')[0]}",
        labels={
            x_axis_col: x_axis_label,
            y_axis_col: y_axis_label
        }
    )


    fig.update_layout(
        template="plotly_white",
        height=480
    )


    st.plotly_chart(
        fig,
        use_container_width=True
        width="stretch"
    )


# CLIMATE & DATA INTELLIGENCE

elif page == "5️⃣ Climate & Data Intelligence":

    st.markdown(
        '<div class="section">Climate Pattern Intelligence</div>',
        unsafe_allow_html=True
    )

    # MONTHLY DATA

    monthly = (
        filtered_df
        .assign(
            month=filtered_df[
                "date"
            ].dt.to_period("M")
        )
        .groupby("month")
        .agg(
            temperature=(
                "temp_max_c",
                "mean"
            ),
            rainfall=(
                "rainfall_mm",
                "sum"
            ),
            humidity=(
                "humidity_pct",
                "mean"
            ),
            wind=(
                "wind_speed_kmph",
                "mean"
            )
        )
        .reset_index()
    )


    monthly["month"] = (
        monthly["month"]
        .astype(str)
    )


    c1, c2 = st.columns(2)


    with c1:

        fig = px.line(
            monthly,
            x="month",
            y="temperature",
            markers=True,
            title="Monthly Temperature Pattern",
            labels={
                "temperature":
                "Average Max Temperature (°C)"
            }
        )

        fig.update_layout(
            template="plotly_white",
            height=420
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            width="stretch"

        )


    with c2:

        fig = px.bar(
            monthly,
            x="month",
            y="rainfall",
            title="Monthly Rainfall Pattern",
            labels={
                "rainfall":
                "Total Rainfall (mm)"
            }
        )

        fig.update_layout(
            template="plotly_white",
            height=420
        )

        st.plotly_chart(
            fig,
            use_container_width=True,
            width="stretch"
        )


    # DISTRIBUTION

    st.markdown(
        '<div class="section">Metric Distribution Analysis</div>',
        unsafe_allow_html=True
    )

    metric_map = {
        "Maximum Temperature": "temp_max_c",
        "Minimum Temperature": "temp_min_c",
        "Rainfall": "rainfall_mm",
        "Humidity": "humidity_pct",
        "Wind Speed": "wind_speed_kmph"
    }

    metric_name = st.selectbox(
        "Analysis Metric",
        list(metric_map.keys()),
        key="distribution_metric"
    )

    metric_column = metric_map[metric_name]

    fig = px.histogram(
        filtered_df,
        x=metric_column,
        color="location",
        marginal="box",
        nbins=30,
        title=f"{metric_name} Distribution"
    )


    fig.update_layout(
        template="plotly_white",
        height=450
    )


    st.plotly_chart(
        fig,
        use_container_width=True,
        width="stretch"
    )

    # CORRELATION

    st.markdown(
        '<div class="section">Weather Variable Relationships</div>',
        unsafe_allow_html=True
    )


    correlation_columns = [
        "temp_max_c",
        "temp_min_c",
        "rainfall_mm",
        "humidity_pct",
        "wind_speed_kmph"
    ]


    correlation = filtered_df[
        correlation_columns
    ].corr()


    fig = px.imshow(
        correlation,
        text_auto=".2f",
        aspect="auto",
        color_continuous_scale="RdBu_r",
        zmin=-1,
        zmax=1,
        title="Correlation Matrix"
    )


    fig.update_layout(
        height=520
    )


    st.plotly_chart(
        fig,

        use_container_width=True,

        width="stretch"

    )


    # DATA QUALITY

    st.markdown(
        '<div class="section">Data Quality Intelligence</div>',
        unsafe_allow_html=True
    )


    q1, q2, q3, q4 = st.columns(4)


    with q1:

        st.metric(
            "Completeness",
            f"{completeness:.1f}%"
        )


    with q2:

        st.metric(
            "Missing Cells",
            int(missing_cells)
        )


    with q3:

        st.metric(
            "Duplicate Rows",
            int(
                filtered_df.duplicated().sum()
            )
        )


    with q4:

        st.metric(
            "Unique Days",
            filtered_df["date"].nunique()
        )


    # ANOMALY ANALYSIS

    anomaly_results = []


    for column in NUMERIC_COLUMNS:

        series = filtered_df[
            column
        ].dropna()


        if series.empty:
            continue


        q1_value = series.quantile(0.25)
        q3_value = series.quantile(0.75)

        iqr = q3_value - q1_value

        lower = q1_value - (
            1.5 * iqr
        )

        upper = q3_value + (
            1.5 * iqr
        )


        count = (
            (series < lower)
            | (series > upper)
        ).sum()


        rate = (
            count / len(series)
        ) * 100


        anomaly_results.append(
            {
                "Metric": column,
                "Records": len(series),
                "Potential Anomalies": int(count),
                "Anomaly Rate (%)": round(
                    rate,
                    2
                )
            }
        )


    anomaly_df = pd.DataFrame(
        anomaly_results
    )


    st.dataframe(
        anomaly_df,
        use_container_width=True,
        width="stretch",
        hide_index=True
    )


    st.caption(
        "IQR anomalies are indicators for analytical review. "
        "They are not automatically treated as incorrect observations."
    )


# DOWNLOAD

st.divider()

st.markdown(
    '<div class="section">📥 Export Current Analysis</div>',
    unsafe_allow_html=True
)


csv_data = filtered_df.to_csv(
    index=False
).encode("utf-8")


st.download_button(
    "Download Filtered Dataset",
    data=csv_data,
    file_name="atmosync_filtered_analysis.csv",
    mime="text/csv"
)

# FOOTER

st.html(dedent("""
    <div class="footer">
        <b>AtmoSync</b>
        · Micro-Climate Analytics & Location Intelligence
        <br>
        Data Engineering · Analytics · Visualization · Data Quality
    </div>
    """))