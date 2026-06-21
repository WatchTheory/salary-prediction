# Salary Prediction Analysis 
><i>A machine learning project that explores what drives salary differences across data analyst roles — from Junior to Senior — using a real-world messy dataset, end-to-end data cleaning, and a multi-model regression pipeline.</i>


## Project Overview
- [Business Requirements](#business-requirements)
- [Dataset](#dataset)
- [Key Findings](#key-findings-in-progress)
- [Tools & Technology](#tools--technology)
- [Model](#model)
- [Project Strucuture](#project-structure)
- [Screenshots](#screenshots)
- [How to Run the Project](#run-the-project)
- [What I'd Improve with more Time](#what-id-improve-with--more-time)


## Business Requirements
What is a fair data-backed salary range for data analysts roles across the U.S - from entry-level to senior - and which factors influeneces compensation the most?
<br>
The project was motivated by a practical job-search problem : salary transparency in the data analyst market, where every salary is different. Job postings use vague ranges, companies vary widely by size and location, and experience levels aren't standardized. The goal was to build a model that could take known inputs (job title, experience level, location, company size, employment type) and return a salary estimate grounded in real market data.

Goals
- Clean a deliberately messy, real-world-style dataset without losing analytical integrity
- Engineer features that capture geographic cost-of-living differences across U.S. cities
- Train and compare four regression models (XGBoost, LightGBM, RandomForest, DecisionTree) using sklearn Pipelines
- Identify which features carry the most salary signal
- Document findings and limitations transparently for future iteration




## Dataset
| Propery         | Details             |
| --------------- | ------------------- |
| Rows            | 2501 Job titles     |
| Columns         | 11 Features         |
| Target Variable | Salary( annual USD) |

> [!Note]
The `messy_data_analyst_job.csv` is to practice this end-to-end data cleaning and modeling because I couldn't find a dataset to use and that was free, I generated a synthetic dataset modeled on real job posting distributions and real location.

> [!Note]
`messy_data_analyst_job.csv` designed to simulated real-world data quality issues. 

## Key Findings

All four models produced low or negative test R² scores, with RandomForest performing best at −0.0076. A negative R² means the model performs worse than simply predicting the mean salary for every row. Rather than treating this as a failure, it points directly to a data quality problem that is worth understanding.


**R2 Results**
| Models         | Train | Test  | OverFit Gap |
| -------------- | ----- | ----- | ----------- |
| XGBoost        | 0.23  | -0.09 | High        |
| Random Forrest | 0.11  | -0.07 | Ok          |
| Decision Tree  | 0.07  | -0.10 | Ok          |
| LightGBM       | 0.47  | -0.22 | High        |


**Why the low score**
 1. Random location imputation introduced noise into the strongest features. The source dataset had significant location column contamination (salary values, skill lists, and employment types ending up in the location field). After cleaning, missing locations were filled with random.choice() across 27 U.S. cities. This means the cost-of-living index and cost tier features — derived directly from location — carry random noise rather than real geographic signal. Location is typically the most predictive feature in a salary dataset, so this is the primary performance bottleneck.
 2. Coarse ordinal encodings compress the salary signal. Mapping job titles to a 1–6 integer scale (Junior → 1, Senior → 6) imposes an artificial linear relationship that may not match actual salary gaps between roles. The same applies to experience level (0–4) and company size (0–4).
 3. The source dataset is synthetic and small. The dataset was generated to simulate messy real-world data. At ~1,865 rows with noisy labels, there is limited signal for a model to generalize from.
 4. RandomForest mean convergence. With weak features, RandomForest's averaging mechanism causes all predictions to cluster around the dataset mean (~$95–100k), regardless of whether the actual salary is $50k or $195k. This is a known behavior, not a bug.

<i>...So what dose this mean.</i>

What this means: The cleaning pipeline, feature engineering approach, and modeling architecture built here are sound. The same pipeline applied to a higher-quality dataset (real job postings, verified salaries) is expected to produce meaningfully better R² scores. The work done here is the foundation.


## Tools & Technology

| Purpose           | Purpose                                 |
| ----------------- | --------------------------------------- |
| Data Manipulation | Pandas, Numpy                           |
| Machine Learning  | scikit-learn, xgboost, lightgbm                                        |
| Visualization     | matplotlib, seaborn                     |
| Outlier Detection | Data Visualization                      |
| Scikit-learn      | IQR-based thresholding(custom function) |
| Pipeline          | Sklearn Pipeline |




## Model

<!-- Phase 1: Baseline Testing (Failed) $\rightarrow$ Phase 2: Feature Engineering & Tuning (In-Progress) -->
**Pipeline diagram**
![Pipeline](/images/ml_pipeline_four_models.png)



## Project Structure

```python
salary-prediction-project/
├── data/           
│   ├── raw/                                     # Raw dataset
│   |    ├── messy_data_analyst_jobs.csv       
│   │    
│   ├── cleaned/                                     # Cleaned datasets
│          ├── Cleaned_data_analyst_jobs.csv/
│          ├── Cost-of-Living-Cities(CLI).csv
├── notebooks/                                      # All notebooks
│   ├── Geolocation-python.ipynb/                    
│   ├── Salary-Prediction.ipynb/                    # Main  notebook
│  
├── sql/
│   ├── schema.sql                # SQL Schema
│   ├── analysis_queries.sql      # SQL Queries
│ 
├── README.md               # ReadMe File            
├── requirements.txt        # Required tools to run the project
```

## Screenshots
SQL
![SQL-Server](/images/resume_project_4.jpg)


## Run The Project

1.Clone the repository
```python
git clone https://github.com/WatchTheory/salary-prediction.git
cd salary-prediction
```
2.Install dependencies
If you haven't already install [uv](https://docs.astral.sh/uv/#projects)

```python
pip install pandas numpy scikit-learn xgboost lightgbm matplotlib seaborn tabulate
```
3. Run Jupyter 
```python
Salary-Prediction.ipynb
```


### Skills Demostrated
- Data wrangling — multi-format cleaning across 8 columns, regex, custom functions, cross-column contamination handling
- Feature engineering — ordinal encoding, geographic cost-of-living index, IQR outlier thresholding
- ML pipeline design — sklearn Pipeline with imputer + scaler + model, fit isolation to training data only
- Model comparison — parallel training and evaluation of 4 regressors, train/test R² with overfit gap analysis
- Analytical communication — documented limitations, root cause analysis, and next-step roadmap




## What I'd Improve with  more Time
- Replace synthetic data with verified salary data (DOL H-1B disclosures or BLS OES data)
- Drop rows with missing locations rather than random-fill, to preserve geographic signal integrity
- Log-transform the salary target — salary distributions are right-skewed, and log-scale regression typically improves performance
- One-hot encode job titles and skills instead of ordinal mapping
- Add k-fold cross-validation for more reliable performance estimates
- Add a Ridge regression baseline to isolate whether poor scores are a feature problem or a model problem

<br>
<i>Part of an active data science portfolio</i> 