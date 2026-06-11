# Salary Prediction Analysis (In Progress)
><i>Cleaned and analyzed 2,500+ synthetic data analyst job postings to surface salary trends by location, experience, company size and skills</i>


## Project Overview

- [Key Findings]()
- [Dataset]()
- [Tools & Technology]()
- [Project Strucuture]()
- [Methodology]()
- [Machin Learning Model]()
- [Business Recommendations]()
- [How to Run]()
- [What I'd Improve with  more Time]()



## Key Findings (In Progress)





## Dataset

> [!WARNING]
The `messy_data_analyst_job.csv` dataset is fake data created by me only for this project.

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





## Project Structure

```python
salary-prediction-project/
├── data/           
│   ├── raw/          # Raw dataset
│   ├── cleaned/      # Cleaned datasets
│
├── notebooks/        # All notebooks
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



## Methodology 
> Note
Rename this to Methodology or Approach. "What the notebook covers" sounds like a table of contents; "Methodology" sounds like an analyst wrote it. Walk through each cleaning decision briefly — not just what you did, but why.




## Machine Learning Model (In Progress)





## Business Recommendations (In Progress)







## Run The Project
> Note
Keep this but add the exact commands. No vague "install the requirements

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
