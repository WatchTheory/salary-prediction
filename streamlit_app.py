"""
Salary Prediction Dashboard
Portfolio project by Casey (github.com/WatchTheory)

Run with: streamlit run app.py
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Data Analyst Salary Explorer",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    /* Card style for KPI metrics */
    [data-testid="metric-container"] {
        background: #1e2329;
        border: 1px solid #2d333b;
        border-radius: 10px;
        padding: 16px;
    }
    [data-testid="metric-container"] label { color: #8b949e; font-size: 0.82rem; }
    [data-testid="metric-container"] [data-testid="stMetricValue"] {
        color: #58a6ff; font-size: 1.6rem; font-weight: 700;
    }
    /* Sidebar */
    section[data-testid="stSidebar"] { background: #161b22; }
    /* Section headers */
    h2 { color: #f0f6fc !important; border-bottom: 1px solid #2d333b; padding-bottom: 6px; }
    h3 { color: #c9d1d9 !important; }
    /* Hero banner */
    .hero { background: linear-gradient(135deg, #0d1117 0%, #161b22 100%);
            border: 1px solid #30363d; border-radius: 12px;
            padding: 28px 32px; margin-bottom: 24px; }
    .hero h1 { color: #58a6ff; margin: 0 0 6px; font-size: 2rem; }
    .hero p  { color: #8b949e; margin: 0; font-size: 0.95rem; }
    .badge { display: inline-block; background: #21262d; color: #79c0ff;
             border: 1px solid #388bfd66; border-radius: 20px;
             padding: 2px 10px; font-size: 0.78rem; margin: 6px 4px 0 0; }
</style>
""", unsafe_allow_html=True)


# ── Data loader ───────────────────────────────────────────────────────────────
@st.cache_data
def load_data(path: str = "data/cleaned/Cleaned_data_analyst_jobs.csv") -> pd.DataFrame:
    df = pd.read_csv(path)

    # ── Normalise common column-name variants ──
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

    # Salary: accept salary, annual_salary, salary_usd, avg_salary, etc.
    salary_candidates = [c for c in df.columns if "salary" in c]
    if salary_candidates and "salary" not in df.columns:
        df = df.rename(columns={salary_candidates[0]: "salary"})

    # Experience level
    exp_candidates = [c for c in df.columns if "exp" in c or "level" in c or "seniority" in c]
    if exp_candidates and "experience_level" not in df.columns:
        df = df.rename(columns={exp_candidates[0]: "experience_level"})

    # Location / state / city
    loc_candidates = [c for c in df.columns if "locat" in c or "state" in c or "city" in c]
    if loc_candidates and "location" not in df.columns:
        df = df.rename(columns={loc_candidates[0]: "location"})

    # Company size
    size_candidates = [c for c in df.columns if "size" in c or "company" in c]
    if size_candidates and "company_size" not in df.columns:
        df = df.rename(columns={size_candidates[0]: "company_size"})

    # Skills (might be a pipe/comma-separated string)
    skill_candidates = [c for c in df.columns if "skill" in c or "tech" in c or "tool" in c]
    if skill_candidates and "skills" not in df.columns:
        df = df.rename(columns={skill_candidates[0]: "skills"})

    # Coerce salary to numeric, drop rows where we can't parse it
    if "salary" in df.columns:
        df["salary"] = pd.to_numeric(df["salary"], errors="coerce")
        df = df.dropna(subset=["salary"])

    return df


try:
    df_raw = load_data()
except FileNotFoundError:
    st.error(
        "⚠️  `Cleaned_data_analyst_jobs.csv` not found. "
        "Make sure the CSV is in the same directory as this script."
    )
    st.stop()


# ── Sidebar – filters ─────────────────────────────────────────────────────────
with st.sidebar:
    st.image(
        "https://avatars.githubusercontent.com/u/50931847?v=4",
        width=72,
    )
    st.markdown("### Casey · WatchTheory")
    st.markdown(
        "[📓 View Notebook](https://github.com/WatchTheory/salary-prediction)  "
        "[👤 GitHub](https://github.com/WatchTheory)",
        unsafe_allow_html=True,
    )
    st.divider()
    st.header("🔍 Filters")

    # Salary range slider
    sal_min, sal_max = int(df_raw["salary"].min()), int(df_raw["salary"].max())
    salary_range = st.slider(
        "Salary Range ($)",
        min_value=sal_min,
        max_value=sal_max,
        value=(sal_min, sal_max),
        step=5_000,
        format="$%d",
    )

    # Experience level
    if "experience_level" in df_raw.columns:
        exp_opts = sorted(df_raw["experience_level"].dropna().unique().tolist())
        exp_sel = st.multiselect("Experience Level", exp_opts, default=exp_opts)
    else:
        exp_sel = None

    # Location
    if "location" in df_raw.columns:
        loc_opts = sorted(df_raw["location"].dropna().unique().tolist())
        loc_sel = st.multiselect("Location", loc_opts, default=loc_opts)
    else:
        loc_sel = None

    # Company size
    if "company_size" in df_raw.columns:
        size_opts = sorted(df_raw["company_size"].dropna().unique().tolist())
        size_sel = st.multiselect("Company Size", size_opts, default=size_opts)
    else:
        size_sel = None

    st.divider()
    st.caption("Dashboard built with Streamlit + Plotly")


# ── Apply filters ─────────────────────────────────────────────────────────────
df = df_raw[df_raw["salary"].between(salary_range[0], salary_range[1])].copy()

if exp_sel is not None:
    df = df[df["experience_level"].isin(exp_sel)]
if loc_sel is not None:
    df = df[df["location"].isin(loc_sel)]
if size_sel is not None:
    df = df[df["company_size"].isin(size_sel)]


# ── Hero banner ───────────────────────────────────────────────────────────────
st.markdown(f"""
<div class="hero">
  <h1>💼 Data Analyst Salary Explorer</h1>
  <p>Cleaned and analysed {len(df_raw):,} synthetic data analyst job postings to surface
     salary trends by location, experience, company size, and skills.</p>
  <span class="badge">Python</span>
  <span class="badge">pandas</span>
  <span class="badge">scikit-learn</span>
  <span class="badge">XGBoost</span>
  <span class="badge">LightGBM</span>
  <span class="badge">Plotly</span>
</div>
""", unsafe_allow_html=True)


# ── KPI row ───────────────────────────────────────────────────────────────────
k1, k2, k3, k4, k5 = st.columns(5)

with k1:
    st.metric("Median Salary", f"${df['salary'].median():,.0f}")
with k2:
    st.metric("Mean Salary", f"${df['salary'].mean():,.0f}")
with k3:
    st.metric("Max Salary", f"${df['salary'].max():,.0f}")
with k4:
    st.metric("Min Salary", f"${df['salary'].min():,.0f}")
with k5:
    st.metric("Job Postings", f"{len(df):,}")

st.markdown("<br>", unsafe_allow_html=True)


# ── Row 1: Salary distribution + box-plot by experience ──────────────────────
st.subheader("📊 Salary Distribution")
col1, col2 = st.columns([1.4, 1])

with col1:
    fig_hist = px.histogram(
        df, x="salary", nbins=40,
        color_discrete_sequence=["#388bfd"],
        labels={"salary": "Annual Salary ($)"},
        title="Salary Distribution",
    )
    fig_hist.update_layout(
        plot_bgcolor="#0d1117", paper_bgcolor="#0d1117",
        font_color="#c9d1d9", bargap=0.05,
        xaxis=dict(gridcolor="#21262d"), yaxis=dict(gridcolor="#21262d"),
    )
    fig_hist.add_vline(
        x=df["salary"].median(), line_dash="dash", line_color="#f78166",
        annotation_text=f"Median ${df['salary'].median():,.0f}",
        annotation_font_color="#f78166",
    )
    st.plotly_chart(fig_hist, use_container_width=True)

with col2:
    if "experience_level" in df.columns:
        fig_box = px.box(
            df, x="experience_level", y="salary",
            color="experience_level",
            color_discrete_sequence=px.colors.qualitative.Bold,
            labels={"salary": "Salary ($)", "experience_level": "Experience"},
            title="Salary by Experience Level",
        )
        fig_box.update_layout(
            showlegend=False,
            plot_bgcolor="#0d1117", paper_bgcolor="#0d1117",
            font_color="#c9d1d9",
            xaxis=dict(gridcolor="#21262d"), yaxis=dict(gridcolor="#21262d"),
        )
        st.plotly_chart(fig_box, use_container_width=True)
    else:
        st.info("No `experience_level` column found in the dataset.")


# ── Row 2: Salary by location ─────────────────────────────────────────────────
if "location" in df.columns:
    st.subheader("📍 Salary by Location")
    top_n = st.slider("Show top N locations", 5, 30, 15, key="loc_slider")
    loc_stats = (
        df.groupby("location")["salary"]
        .agg(median="median", count="count")
        .reset_index()
        .sort_values("median", ascending=False)
        .head(top_n)
    )
    fig_loc = px.bar(
        loc_stats, x="median", y="location", orientation="h",
        color="median",
        color_continuous_scale="Blues",
        hover_data={"count": True, "median": ":$,.0f"},
        labels={"median": "Median Salary ($)", "location": "Location", "count": "# Postings"},
        title=f"Top {top_n} Locations by Median Salary",
    )
    fig_loc.update_layout(
        plot_bgcolor="#0d1117", paper_bgcolor="#0d1117",
        font_color="#c9d1d9", coloraxis_showscale=False,
        yaxis=dict(autorange="reversed", gridcolor="#21262d"),
        xaxis=dict(gridcolor="#21262d"),
        height=420,
    )
    st.plotly_chart(fig_loc, use_container_width=True)


# ── Row 3: Company size + correlation heatmap ─────────────────────────────────
col3, col4 = st.columns(2)

with col3:
    if "company_size" in df.columns:
        st.subheader("🏢 Salary by Company Size")
        size_stats = (
            df.groupby("company_size")["salary"]
            .agg(median="median", q25=lambda x: x.quantile(0.25),
                 q75=lambda x: x.quantile(0.75), count="count")
            .reset_index().sort_values("median", ascending=False)
        )
        fig_size = px.bar(
            size_stats, x="company_size", y="median",
            error_y=size_stats["q75"] - size_stats["median"],
            color="median", color_continuous_scale="Teal",
            labels={"median": "Median Salary ($)", "company_size": "Company Size"},
            title="Median Salary by Company Size",
        )
        fig_size.update_layout(
            plot_bgcolor="#0d1117", paper_bgcolor="#0d1117",
            font_color="#c9d1d9", coloraxis_showscale=False,
            xaxis=dict(gridcolor="#21262d"), yaxis=dict(gridcolor="#21262d"),
        )
        st.plotly_chart(fig_size, use_container_width=True)

with col4:
    st.subheader("📐 Numeric Feature Correlation")
    num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
    if len(num_cols) >= 2:
        corr = df[num_cols].corr()
        fig_heat = px.imshow(
            corr, text_auto=".2f",
            color_continuous_scale="RdBu", zmin=-1, zmax=1,
            title="Correlation Matrix",
        )
        fig_heat.update_layout(
            plot_bgcolor="#0d1117", paper_bgcolor="#0d1117",
            font_color="#c9d1d9",
        )
        st.plotly_chart(fig_heat, use_container_width=True)
    else:
        st.info("Not enough numeric columns for a correlation heatmap.")


# ── Row 4: Skills analysis ────────────────────────────────────────────────────
if "skills" in df.columns:
    st.subheader("🛠️ In-Demand Skills & Salary Impact")

    # Explode comma/pipe/semicolon-separated skills
    skill_df = df[["skills", "salary"]].dropna(subset=["skills"]).copy()
    skill_df["skills"] = skill_df["skills"].str.split(r"[,|;/]")
    skill_df = skill_df.explode("skills")
    skill_df["skills"] = skill_df["skills"].str.strip().str.title()
    skill_df = skill_df[skill_df["skills"].str.len() > 1]

    skill_stats = (
        skill_df.groupby("skills")
        .agg(count=("salary", "count"), median_salary=("salary", "median"))
        .reset_index()
        .sort_values("count", ascending=False)
        .head(20)
    )

    c5, c6 = st.columns(2)
    with c5:
        fig_skill_cnt = px.bar(
            skill_stats.sort_values("count"), x="count", y="skills",
            orientation="h", color="count", color_continuous_scale="Purples",
            title="Top 20 Most Mentioned Skills",
            labels={"count": "# Job Postings", "skills": "Skill"},
        )
        fig_skill_cnt.update_layout(
            plot_bgcolor="#0d1117", paper_bgcolor="#0d1117",
            font_color="#c9d1d9", coloraxis_showscale=False,
            yaxis=dict(autorange="reversed", gridcolor="#21262d"),
            xaxis=dict(gridcolor="#21262d"), height=500,
        )
        st.plotly_chart(fig_skill_cnt, use_container_width=True)

    with c6:
        fig_skill_sal = px.bar(
            skill_stats.sort_values("median_salary"), x="median_salary", y="skills",
            orientation="h", color="median_salary", color_continuous_scale="Greens",
            title="Median Salary by Skill",
            labels={"median_salary": "Median Salary ($)", "skills": "Skill"},
        )
        fig_skill_sal.update_layout(
            plot_bgcolor="#0d1117", paper_bgcolor="#0d1117",
            font_color="#c9d1d9", coloraxis_showscale=False,
            yaxis=dict(autorange="reversed", gridcolor="#21262d"),
            xaxis=dict(gridcolor="#21262d"), height=500,
        )
        st.plotly_chart(fig_skill_sal, use_container_width=True)


# ── Row 5: Raw data explorer ──────────────────────────────────────────────────
st.subheader("🗂️ Data Explorer")
with st.expander("View & search raw data", expanded=False):
    search = st.text_input("Search across all columns", "")
    display_df = df if not search else df[
        df.apply(lambda r: r.astype(str).str.contains(search, case=False).any(), axis=1)
    ]
    st.dataframe(
        display_df.sort_values("salary", ascending=False).reset_index(drop=True),
        use_container_width=True,
        height=350,
    )
    st.caption(f"Showing {len(display_df):,} of {len(df_raw):,} rows")


# ── Footer ─────────────────────────────────────────────────────────────────────
st.divider()
st.markdown(
    "<center style='color:#484f58; font-size:0.82rem;'>"
    "Built by <b>Casey</b> · "
    "<a href='https://github.com/WatchTheory/salary-prediction' style='color:#58a6ff;'>"
    "github.com/WatchTheory/salary-prediction</a>"
    "</center>",
    unsafe_allow_html=True,
)
