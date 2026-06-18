
# Notes

## Overview

- [Problem]()
- [The Solution]()
    1. Choosing a Model
       - why I choose the model 
     2. Choose a Encoder 
     3. Market Index








**Background:** 
I have dataframe of synthetic data full of data analyst salaries that 
that has `job_title`, 'salary' , 'location', `experience`, 'company_size', 'remote_location', 'employment_type' and skills 'skills'


**Requirements:** 
 - The salary *MUST* be a believable as much as possible 
 - The salary should be based off market value in the U.S 
 - The Model should be able to predict salary for all data analyst job titles



**Equation:** 
You can think of the equation of what we are trying to solve for.
$$
Salary = title + location + Experience
$$

For Reference: of what the dataset looks before

Before:

|  job_title             |  salary    |  location     |  experience | 
|------------------------|------------|---------------|-------------|
| Junior Data Analyst    |    0       | Las Vegas, NV |     Jr      | 
| Senior Data Analyst    |   65,000   | New York, NY  |     Sr      |
| Marketing Data Analyst |   95,000   | Phonenix, AZ  |    None     |


----

### Problem 
**Problem:** Some jobs in the dataset don't match realistic values (for example "junior data analyst") would never be paid $0 in Las Vegas. In order to make sure this data can be presented *realistic*. The salary column needs to be formated to *realistic* or *bealivable* values.  

**Objective** : You need find a way to make the salaries more realistic to the job & location
 
For Reference: of what we are trying to get the dataset to look like at the end.

After:
|  job_title             |  salary    |  location     |  experience | 
|------------------------|------------|---------------|-------------|
| Junior Data Analyst    |   65,000   | Las Vegas, NV |     Jr      | 
| Senior Data Analyst    |   120,000  | New York, NY  |     Sr      |
| Marketing Data Analyst |   85,000   | Phonenix, AZ  |    None     |

----

### The Solution : 

```
- Choose XGBoost Model
- Choose Label Encode  
   - Found Better way: 
      - Use lat/lon of citie airport.
      
         - Note: Some cities have two multiple airports, so will use my best judgement when decising on the which airports to use.
   - Create new column of airports lat/lon in dataframe 
```


**Steps**
**1.Choose A Model**
  - **Linear Regression**
    - What Dose Linear Regression do?
       - Linear regression is a statistical technique used to find the relationship between variables. In an ML context, linear regression finds the relationship between features and a label. **5 [Linear Regression](https://developers.google.com/machine-learning/crash-course/linear-regression)
          - <u>The model is a linear model</u>
          - The prediction is a floating-point value
    - Advantages 
      - The true relationship is approximately linear or can be made linear via transformations (log, Box-Cox, etc.).
      - The number of predictors (p) is not extremely large (relative to (n)), or if large, many have small/no effect.
      - Variables are on continuous or ordered scales (dummy coding allows inclusion of categorical dummies, though interactions may be needed).
      - Good baseline, Interpretable
      - Errors are roughly homoscedastic and uncorrelated.
      - Model interpretability is important (e.g. economics, social science).
      - Noise is moderate, without extreme outliers or heavy tails.
    - Limitations
      - predicting intrinsically nonlinear phenomena
      - If (p) approaches or exceeds (n), OLS may overfit or be underdetermined
      - Nominal factors require dummy encoding. If many categories or interactions, the model can become unwieldy.
      - OLS is not robust; a few extreme (y) values can dominate the fit
      - If error variance grows with (x), OLS standard errors are invalid; weighted least squares or variance-stabilizing transformations are needed.
      - If many intricate interactions affect (y), including all in a linear model may be difficult. Tree or ensemble methods can capture interactions automatically.
    - Good at: 
       - House prices predictions
       - Dose-Response in Biology
       - Economics (Trend Forecasting)
       - predicting what comes next
    - Bad At:
       - Image/Signal Classification:
       - Speech Recognition:
       - Stock Price Prediction
       - uncertainity 

  2. **Ridge/Lasso Regression**
      - Was not considered

 3. **Random Forest**
     - What Dose Random Forrest Do?
        - Handles non-linear relationships, very accurate

 4. **Gradient Boosting(XGBoost)**
     - What Dose XBoost Do?
        - Best accuracy for tabular data like this
        - machine learning algorithm under ensemble learning and It is trendy for supervised learning tasks
        - It utilizes decision trees as base learners and employs regularization techniques to enhance model generalization
        - ==<u>The algorithm works by sequentially adding weak learners to the ensemble, with each new learner focusing on correcting the errors made by the existing ones.</u>==
        - include its ability to handle complex relationships in data, ==regularization techniques to prevent overfitting== and incorporation of parallel processing
        - it builds an ensemble of decision trees sequentially, where each new tree corrects the errors of the previous ones
        - Easy to install boosting library 
    - The bad 
        - languages are chosen for their speed and efficiency, which are critical for handling large datasets. they are not as accessible for Python, which has become the language of choice for many researchers due to its ease of use and readability. 
        - limited evolution of the core algorithm, implementation barriers due to low-level languages, and a lack of modularity


**<u>Why did you choose that Model?</u>**

Gradient Boosting (XGBoost)
 - Best for accuracy 
 - works well with tabular data - tree-based models are well-suited for capturing patterns in tabular data without requiring sophisticated preprocessing or extensive feature engineering
 - Handling raw data - gradient boosted trees can typically process raw data with little or no adjustment.
 - Handles null values - many popular gradient boosting frameworks can handle missing values automatically, either by assigning them to a separate branch during training or learning optimal splits for null values. (If I did the work correctly, we won't have any null values but that also good to know )
 - Train faster using GPU - When processing large datasets, gradient boosting libraries can also take advantage of modern hardware, including GPUs, to train models faster


When using different models Random Forest (Runner-Up) will be used because its a tree-structure format, which will be good for what I am trying to do. Also Linear Regression will can be used for a baseline or starting point.


Elimiated Models
- Linear Regression : During my research I am trying to predict salaries and one of the advanatage of `Linear Regression` is it works best when the data is linear. The data I am doing is <u>**not at all linear**</u>. Another issue, is that it doesn't handle outliers very well and is very senstive to outliers, the data I am working with will have mostly like have outliers, for example Senior Data Analyst pay is `$50` vs Junior Analyst `$90,000`. When your working in (thousands) the $50 will be the outliers. The Model would be good to use for a baseline

----


**2.Choose A Encoder (For Machine Learning)**
  - Label Encode : Converts target variables (classes) into integers (0 to n-1); not recommended for predictor variables as it implies false ordinality. 
  - Hot-One Encode : Creates binary columns for each category; ideal for nominal data with few categories
  - Binary Encoder : Eliminated 
  - Count Encoding : Eliminated 
  - LeaveOneOut Encoder: A supervised method that prevents overfitting by calculating the mean target value while excluding the current row.
   
Eliminated Encoders
  - Binary Encoder: used for High efficient dimensional data 
  - Count Encoder : Replaces categories with the frequency count of their occurrences in the dataset
 

 $$
  0 (Entry) -----> 1 (Mid) ------> 2(Senior) -------> 3 (Lead)
 $$
- Higher integer = more experience — the model can now learn "`salary tends to rise with experience`"

<br>

<u>Why did you choose that Encode:</u> 
   - Best choice: Label Encode  
     - map to explicit integers that preserve order (Entry=0, Mid=1, Senior=2, Lead=3).
     - integers have an implied size relationship (3 > 2 > 1 > 0), and want the relationship to match reality.
     - is to define the order yourself before encoding, using either OrdinalEncoder(categories=[...]) from scikit-learn or a simple pandas .map() dict. Both give the same result — the pandas .map() approach is often cleaner to read and easier to debug.
---


**3.Research market job index - cost of living index score**
 - How to tie in airport geo lat/lon to cost of living index



Source : 
 - [Kaggle](https://www.kaggle.com/datasets/lukkardata/cost-of-living-missouri-economic-research)
 - [Zillow](https://www.zillow.com/home-values/102001/united-states/)
 - [Numbeo](https://www.numbeo.com/cost-of-living/country_result.jsp?country=United+States)




**Geolocation**

- Using python, create python script to get the geolocation for these respect, after viewing the geolocation
- Create new pandas dataframe to map the geolocation to the correct cities then, add the two columns to bdata dataframe




**5.Encode Text Column Job Title**

1. Define the order yourself for the `Experience` Column before encoding using either `OrdinalEncoder(categories[...])` from scikit-learn or a simple pandas `.map` approach. The same logic applies to `company_size` (Small=0, Medium=1, Large=2) 

**Problem:**
We found a way to Encode the `company_size` and the `Experience` column but not the `Location` column. So 
  - How do you index major cities in the U.S?
     1. We could use Leave-One-Out Encode for location
     or 
     2. See **Note 3 and **Note 4





---

==Note 3==:  When it came time to finding a way to encode the `location` column, at the time there was only which was using Leave-one-Out Encode. Now I was like " I can think of something better to use", so I came up with a genius and creative idea.

Here is the problem, I wanted to encode the `location` column with Label Encoder after some research that wasn't going to work out so well. I have to find a better way at encoding the major cities in the U.S. Since the major cities don't have real order to them, I need to find a way to index the major cities.

The answer: airports, I don't want to use the major cities but the airport code , more specificly the airport lat/lon coordinates. See every airport has a 3 letter code in the U.S, for example the LAX is Los Angeles Aiport, in order to become a airport you need to be given a 3 digit letter by the IATA (which is located in Canada) or the IATA airpot codes these special 3 letters 
for location identification in the 1930, back then the U.S used the two-letters code for the National Weather Service (NWS)
to identify cities.

==Note 4==:I won't worry about cost of living and local labour demand for the cities that may come later.

---



**6.Predict Salary Values for Salary Column**




**6.5.How to fill in salary values from Model?**




-----------------------------------------------------------

## Solution Notes 

Note 1: Building  Solution list order - When building the solution I first created 2 list, the first list is the steps for the solution and then created a second list. This list is a temp list, only going to hold task or objection that I don't know where they will go on the Solution list. Because I know these items will have to get done, in order to complete the project. I can safetly put them in a temp list till I know where they will go.

Note 2: Because no solution is generic, I added questions to the problem that I will end up having to answer sooner or later, I added them to the solution list because I don't what there to be any uncertain in the solution. These question will help guide me in creating the solution. The point of these solution is to bridge some of the gap between objective ( for example objective 5 and objective 6) and kinda like adding flashlights to a dark room to make the room more illuminate. Over time the flashlights will move to something more permanent, kinda like when explore a dark cave, explorers will set down glow sticks to light there way and over time a team will follow the lights and replace them with stronger and more powerful lights to light the way to the dig site. For now we are lighting our path with glow sticks.

-----------------------------------------------------------

Unrelated Information

```python
from sklearn.preprocessing import LabelEncoder
import xgboost as xgb                                
from sklearn.model_selection import train_test_split  
from sklearn.metrics import accuracy_score
```



Why Use Encode Text Columns?

- Machine Learning model reqirie numerical input and can't use directly process ( simple terms - Linear regression can't use text and can only use numbers), thus we need to use convert our `job_title` column to numbers. 
  
 
 
1.Label Encoding 
 - Label Encoding assigns a unique number to each category. In our example, we could assign the number 1 to Poor, 2 to Fair, and so on. So, your list of customer feedback would become [1, 2, 3,4,5]. **1 [Label Encoding vs One-Hot Encoding](https://medium.com/aimonks/label-encoding-vs-one-hot-encoding-making-sense-of-categorical-data-1181914501f3)

 - Pros  - Good with Order like "low", "Medium", "High"
 Label Encoding is great when you have categories with an inherent order or rank, like ‘low,’ ‘medium,’ and ‘high’ in a survey response. However, it has a drawback when used for nominal categories, such as colors, because it can imply an unintended order. **2 [Label Encoding vs One-Hot Encoding](https://medium.com/aimonks/label-encoding-vs-one-hot-encoding-making-sense-of-categorical-data-1181914501f3)




2.One-Hot Encoding
- One-hot encoding is a method of converting categorical variables into a format that can be provided to machine learning algorithms to improve prediction. It involves creating new binary columns for each unique category in a feature. Each column represents one unique category, and a value of 1 or 0 indicates the presence or absence of that category. *3 [What Is One Hot Encoding and How to Implement It in Python](https://www.datacamp.com/tutorial/one-hot-encoding-python-tutorial) 

- Pros - transform categorical data [Text data] into a seperate column to be used for on a machine learning Model.

- For example, assigning 1 to Red, 2 to Green, and 3 to Blue could make the model think that Green is greater than Red and Blue is greater than both. This misunderstanding can negatively affect the model's performance.One-hot encoding solves this problem by creating a separate binary column for each category. This way, the model can see that each category is distinct and unrelated to the others. 



### Best Practices & Considerations

- Hot-Encoding in Scikit-leanr [One Hot Encoding Using Scikit-Learn](https://builtin.com/articles/one-hot-encoding)
- Hot-Encoding in Pandas [One Hot Encoding in Pandas](https://builtin.com/articles/one-hot-encoding)


Using the `raw` version of OneHotEncoder, i.e. without a column transformer, needs the most manual adjustment, and I only see rare cases in which I would use this approach in practice.
If your process relies on scikit pipelines, which has many advantages, then using scikit OneHotEncoder with a column transformer seems to be the most natural choice to me.
If you like to process the data step-by-step, going from DataFrame to DataFrame, which can be a good choice in the exploration phase, then I would definitely take the pandas.get_dummies approach.




### What Machine Learning Model to use 

- Random ForestHandles non-linear relationships, very accurate
- Gradient Boosting (XGBoost)Best accuracy for tabular data like this



# Models  

**XGBoost**  - for supervised machine learning tasks.
 -  uses gradient boosted decision trees, a supervised learning boosting algorithm that makes use of gradient descent. **4.[What is XGBoost?](https://www.ibm.com/think/topics/xgboost)


- Best accuracy for tabular data like this


Featues: 
  - Parallel and distributed computing - The library stores data in in-memory units called blocks. Separate blocks can be distributed across machines
  - Cache-aware prefetching algorithm  - uses a cache-aware prefetching algorithm which helps reduce the runtime for large datasets. The library can run more than ten times faster than other existing frameworks on a single machine
  - Built in regularization - Data may also be regularized through hyperparameter tuning. Using XGBoost’s built in regularization also allows the library to give better results than the regular scikit-learn gradient boosting package.
  - Handling missing values - uses a sparsity-aware algorithm for sparse data. When a value is missing in the dataset, the data point is classified into the default direction and the algorithm learns the best direction to handle missing values.




**The Good & Bad**

Good 
 - 


Bad





**Random Forrest**
-  as an ensemble learning method wherein many decision trees are constructed during training, with the output being either the mean prediction for regression or the mode of the classes for classification. **5 [XGBoost vs. Random Forest vs. Gradient Boosting](https://www.spiceworks.com/soft-tech/xgboost-vs-random-forest-vs-gradient-boosting/)

 - Handles non-linear relationships, very accurate



Features

 
The Good & Bad
Good:
 - Decision trees may be popular supervised learning algorithms but are not immune to problems such as bias and overfitting.


Bad:
 - with multiple decision trees forming an ensemble in Random Forest, more accurate results can be predicted, especially when individual trees are uncorrelated.



