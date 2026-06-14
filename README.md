# Salary Prediction Analysis (In Progress)
><i>Cleaned and analyzed 2,500+ synthetic data analyst job postings to surface salary trends by location, experience, company size and skills</i>


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



## Key Findings (In Progress)



## Dataset

> [!WARNING]
The `messy_data_analyst_job.csv` is to practice this end-to-end data cleaning and modeling because I couldn't find a dataset to use and that was free, I generated a synthetic dataset modeled on real job posting distributions and real location.

Source: 

| Propery  |   Details  |
|-----------|------------|
|   Rows    |  2501 Job titles      |
|   Columns      |     11 Features       |
| Target Variable |  Salary   |



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



## Project Structure

```python
salary-prediction-project/
├── data/           
│   ├── raw/          # Raw dataset
│   ├── cleaned/      # Cleaned datasets
│
├── notebooks/                  # All notebooks
│   ├── data_cleaning.ipynb/    # data cleaning notebook
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
├── Notes.txt               # Deep Dive into the question I asked and how I solved problems.  
├── requirements.txt        # Required tools to run the project
```



## Methodology (In Progress)




## Machine Learning Model (In Progress)



## Business Recommendations (In Progress)




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
- Data Cleaning using SQl
