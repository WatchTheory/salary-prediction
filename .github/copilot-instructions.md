# Copilot Instructions for salary-prediction

This is a Python-based ML project analyzing data analyst salary trends with data cleaning, feature engineering, and multi-model regression pipelines.

## Running the Project

### **Streamlit Dashboard**
```bash
streamlit run streamlit_app.py
```
Launches interactive dashboard with salary filters, distributions, location trends, company size analysis, and skills correlation. Requires `data/cleaned/Cleaned_data_analyst_jobs.csv` to exist.

### **Jupyter Notebooks**
- **Main analysis**: `notebooks/Salary_Prediction.ipynb` — complete ML pipeline (data cleaning → feature engineering → 4-model comparison)
- **Geolocation work**: `notebooks/Geolocation_python.ipynb` — cost-of-living indexing by U.S. city
- **SQL analysis**: `sql/sql_python.ipynb` — schema and exploratory queries

### **Dependencies**
Install via `pyproject.toml` (uses `uv` package manager):
```bash
uv pip install -e .
# or manually:
pip install -r requirements.txt
```

Core packages: pandas, numpy, scikit-learn, xgboost, lightgbm, plotly, streamlit

## Architecture & Data Flow

### **Three Main Entry Points**

1. **Streamlit App** (`streamlit_app.py`)
   - Loads cleaned CSV via `@st.cache_data`-decorated `load_data()` function
   - Handles flexible column naming (normalizes `salary`, `experience_level`, `location`, `company_size`, `skills` variants)
   - Applies sidebar filters (salary range, experience, location, company size) and renders Plotly visualizations

2. **Jupyter Notebooks** (analysis & modeling)
   - `Salary_Prediction.ipynb` orchestrates the full pipeline:
     - Data cleaning: multi-format regex, cross-column contamination handling, custom IQR outlier thresholding
     - Feature engineering: ordinal encoding (job titles 1–6, experience 0–4, size 0–4), geographic cost-of-living index
     - ML pipeline: sklearn `Pipeline` with imputer → scaler → model (isolated to training data only)
     - Model comparison: XGBoost, LightGBM, RandomForest, DecisionTree with train/test R² + overfit gap analysis
   - `Geolocation_python.ipynb` builds cost-of-living features by mapping 27 U.S. cities to cost tiers

3. **SQL Schema & Queries** (`sql/` directory)
   - Optional: for exploratory analytics on the cleaned dataset
   - Schema and queries available in notebooks

### **Data Lifecycle**

- **Raw**: `data/raw/messy_data_analyst_jobs.csv` — synthetic, ~2,501 rows, deliberately messy (contaminated location field, missing values, inconsistent formats)
- **Cleaned**: `data/cleaned/Cleaned_data_analyst_jobs.csv` — output of notebook cleaning pipeline, used by Streamlit
- **Reference**: `data/cleaned/Cost-of-Living-Cities(CLI).csv` — geographic cost-of-living tiers

## Key Conventions & Patterns

### **Data & Feature Engineering**
- **Ordinal encoding philosophy**: Job titles, experience levels, and company size are encoded as integers (1–6, 0–4, 0–4 respectively), imposing linear assumptions—this is a known limitation and candidate for one-hot encoding in future iterations
- **Location handling**: Missing locations currently filled with `random.choice()` across 27 cities (introduces noise); future work should drop rows to preserve geographic signal
- **Salary target**: Annual USD, right-skewed distribution (candidate for log-transform in next phase)
- **Outlier detection**: IQR-based custom function; approach is consistent across all numeric features

### **ML Pipeline Structure**
- Sklearn `Pipeline` with 3 stages: `[imputer, scaler, model]`
- **Critical**: Fit imputer and scaler to training data only (using `fit()` before `transform()`); applied to test data without re-fitting
- 4-model comparison loop: XGBoost, LightGBM, RandomForest, DecisionTree
- Evaluation metric: R² on both train and test; overfit gap = train R² − test R²

### **Streamlit Code Patterns**
- Column normalization: Use lowercase, underscore-separated names; handle variants of `salary`, `experience_level`, `location`, `company_size`, `skills`
- `@st.cache_data` for expensive data loads; clears only on code changes
- Plotly visualizations with dark GitHub theme: `plot_bgcolor="#0d1117"`, `paper_bgcolor="#0d1117"`, `font_color="#c9d1d9"`
- Sidebar filters use `st.multiselect()` with `default=sorted_unique_values()` for consistent ordering
- Always `.dropna()` on key columns before groupby/filtering to prevent NaN propagation

### **Column Naming**
No strict enforced scheme, but dashboard expects these patterns:
- Salary: any column with "salary" in name (auto-normalized to `salary`)
- Experience: "exp", "level", or "seniority" in name → normalized to `experience_level`
- Location: "locat", "state", or "city" in name → normalized to `location`
- Company: "company" or "size" in name → normalized to `company_size`
- Skills: "skill", "tech", or "tool" in name → normalized to `skills`

### **Known Limitations & Next Steps**
- Low R² scores (−0.22 to 0.23) due to: random location imputation adding noise, coarse ordinal encodings, small synthetic dataset
- Not a model failure—same pipeline on high-quality real data (DOL H-1B, BLS OES) expected to improve significantly
- Future improvements: drop missing locations (not fill), log-transform salary, one-hot encode job titles, add k-fold CV, add Ridge baseline

## Testing & Validation

No automated test suite; project is exploratory/portfolio work. Validation via:
- Notebook cell-by-cell execution (visual inspection of outputs)
- Streamlit app filter interactions (manual QA)
- Correlation heatmaps and distribution plots (domain sanity checks)

## Development Notes

- **Python version**: 3.13+ (as per `pyproject.toml`)
- **Package manager**: Prefers `uv` for dependency resolution; pip works as fallback
- **Notebook-first approach**: Primary work happens in Jupyter; Streamlit app consumes cleaned CSV output
- **Git**: Uses standard Git flow; no CI/CD currently configured
