# Salary Prediction Analysis 
><i>Engineered a salary prediction tool using XGBoost on 2,200+ real-world job postings, giving data analysts a data-driven benchmark to negotiate compensation by role, location, and skill set.</i>


## Project Overview

- [Key Findings](#key-findings-in-progress)
- [Dataset](#dataset)
- [Tools & Technology](#tools--technology)
- [Project Strucuture](#project-structure)
- [Methodology](#methodology-in-progress)
- [Machin Learning Model](#machine-learning-model-in-progress)
- [Business Recommendations](#business-recommendations-in-progress)
- [How to Run the Project](#run-the-project)
- [What I'd Improve with more Time](#what-id-improve-with--more-time)


## Dataset

| Propery  |   Details  |
|-----------|------------|
|   Rows    |  2501 Job titles      |
|   Columns      |     11 Features  |
| Target Variable |  Salary   |

> [!Note]
The `messy_data_analyst_job.csv` is to practice this end-to-end data cleaning and modeling because I couldn't find a dataset to use and that was free, I generated a synthetic dataset modeled on real job posting distributions and real location.


## Tools & Technology

|  Tools  |  Purpose      |
|---------|---------|
|  Python | Data Analysis, Data Cleaning, Data Imputation |
|  Numpy  |  Data Imputation  |
|  Pandas |  Data Manipulation  |
|  Seaborn/Mathplib/Plotly  |  Data Visualization       |
|  Scikit-learn      |  Machine Learning Models      |
|   SQL   |  Complex Querying and Analyst     |
|  Google Sheets/Excel |   used for web scrapping data |  



## Model

**Pipeline diagram**
![Pipeline](/images/ml_pipeline_four_models.png)


Phase 1: Baseline Testing (Failed) $\rightarrow$ Phase 2: Feature Engineering & Tuning (In-Progress)



Reduced overfitting by 
1. Reducing data leaks 
2. Simplify train,test, fit process by putting in a pipeline
3. Removing unnescessary and unrealistic rows 


<br>

**R2 Results**
| Models         | Train | Test | OverFit Gap |
| -------------- | ----- | ---- | ----------- |
| XGBoost        | 0.32  |      |             |
| Random Forrest | 0.14  |      |  0.16       |
| Decision Tree  | 0.10  |      |             |
| LightGBM       | 0.53  |      |             |




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
├── src/
│   ├── extract.py
│   ├── transform.py            
│   ├── load.py             # Loaded 
│   ├── train_model.py      # trained Model
│   ├── predict.py          # Salary Predictions Model
│
├── README.md               # ReadMe File            
├── requirements.txt        # Required tools to run the project
```


## Run The Project

1.Clone the repository

2.Install dependencies
```python
pip install -r requirements.txt
```
3. Run Jupyter 
```python
jupyter notebook data_cleaning.ipynb
```
Also runs in google colab
- Download the notebook `ipynb` file 
- Upload file 
- Run All cells


## What I'd Improve with  more Time
Run through claude
- Build a proper salary prediction model 
- Generate more syntic data for forecast model
- Geographic cost-of-living normalization

