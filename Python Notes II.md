
## Notes

**Background:** 
I have dataframe of synthetic data full of data analyst salaries that 
that has `job_title`, 'salary' , 'location', `experience`, 'company_size', 'remote_location', 'employment_type' and skills 'skills'


**Requirements:** 
 - The salary *MUST* be a believable as much as possible 
 - The salary should be based off market value in the U.S 
 - The Model should be able to predict salary for all data analyst job titles


**Equation:** 
> 
    Salary = job_title + location + Experience
    
For Reference
Before:

|  job_title             |  salary    |  location     |  experience | 
|------------------------|------------|---------------|-------------|
| Junior Data Analyst    |    0       | Las Vegas, NV |     Jr      | 
| Senior Data Analyst    |   65,000   | New York, NY  |     Sr      |
| Marketing Data Analyst |   95,000   | Phonenix, AZ  |    None     |

<br>

### Problem 
**Problem:** Some jobs in the dataset don't match realistic values (for example "junior data analyst") would never be paid $0 in Las Vegas. In order to make sure this data can be presented *realistic*. The salary column needs to be formated to *realistic* or *bealivable* values.  

**Objective** : You need find a way to make the salaries more realistic to the job & location
 


After:
|  job_title             |  salary    |  location     |  experience | 
|------------------------|------------|---------------|-------------|
| Junior Data Analyst    |   65,000   | Las Vegas, NV |     Jr      | 
| Senior Data Analyst    |   120,000  | New York, NY  |     Sr      |
| Marketing Data Analyst |   85,000   | Phonenix, AZ  |    None     |


### The Solution : 
```
Job Title (text) → Encode → Numeric
Salary (raw)     → Score/Index → Normalized Numeric
Then feed BOTH into an ML model for better predictions
```


**Steps**

1.Choose A Model 
  - Linear Regression
  - Ridge/Lasso Regression
  - Random Forest
  - Cradient Boosting(XGBoost)


2.Choose A Encoder (For Machine Learning)
  - Label Encode : Converts target variables (classes) into integers (0 to n-1); not recommended for predictor variables as it implies false ordinality. 
  - Hot-One Encode : Creates binary columns for each category; ideal for nominal data with few categories
  - Binary Encoder : Eliminated 
  - Count Encoding : Eliminated 
  - LeaveOneOut Encoder: A supervised method that prevents overfitting by calculating the mean target value while excluding the current row.
   
Eliminated Encoders
  - Binary Encoder: used for High efficient dimensional data 
  - Count Encoder : Replaces categories with the frequency count of their occurrences in the dataset
 

Thoughs : 

I was leading towards Leave-One-Out Encoder because it 1. Reduce Over fitting, I believe it might  happen because some of the position in the location column. 2. Leakage Prevention : Excludes the current observation target ( in this case the targets I feed the model) to caluclate the mean and reduce bias.
```
0 (Entry) -----> 1 (Mid) ------> 2(Senior) -------> 3 (Lead)
```
Higher integer = more experience — the model can now learn "salary tends to rise with experience"


Why did you choose that Encode : 
   - Best choice 
     -- map to explicit integers that preserve order (Entry=0, Mid=1, Senior=2, Lead=3).
     -- integers have an implied size relationship (3 > 2 > 1 > 0), and you want that relationship to match reality.
     -- is to define the order yourself before encoding, using either OrdinalEncoder(categories=[...]) from scikit-learn or a simple pandas .map() dict. Both give the same result — the pandas .map() approach is often cleaner to read and easier to debug.

     

3.Research market job index - cost of living index score




3.5 How to build Salary Score Index?



 
4.Build Salary Score Index






5.Encode Text Column 'Job_titles'




6.Predict Salary Values for Salary Column




6.5.How to fill in salary values from Model?


------------ Not On the List Yet--------------
1. How to fill in salary values from Model
1. 
1. 

-----------------------------------------------------------

## Solution Notes 

Note 1: Building  Solution list order - When building the solution I first created 2 list, the first list is the steps for the solution and then created a second list. This list is a temp list, only going to hold task or objection that I don't know where they will go on the Solution list. Because I know these items will have to get done, in order to complete the project. I can safetly put them in a temp list till I know where they will go.

Note 2: Because no solution is generic, I added questions to the problem that I will end up having to answer sooner or later, I added them to the solution list because I don't what there to be any uncertain in the solution. These question will help guide me in creating the solution. The point of these solution is to bridge some of the gap between objective ( for example objective 5 and objective 6) like adding flashlights to a dark room to make the room more illuminate. Over time the flashlights will move to something more permanent, kinda like when explore a dark cave, explorers will set down glow sticks to light there way and over time a team will follow the lights and replace them with stronger and more powerful lights to light the way. For now we are lighting our path with glow sticks.

-----------------------------------------------------------

Using Text Columns
- from sklearn.linear_model import LinearRegression
- from sklearn.preprocessing import LabelEncoder


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


Using the “raw” version of OneHotEncoder, i.e. without a column transformer, needs the most manual adjustment, and I only see rare cases in which I would use this approach in practice.
If your process relies on scikit pipelines, which has many advantages, then using scikit OneHotEncoder with a column transformer seems to be the most natural choice to me.
If you like to process the data step-by-step, going from DataFrame to DataFrame, which can be a good choice in the exploration phase, then I would definitely take the pandas.get_dummies approach.




### What Machine Learning Model to use 

- Random ForestHandles non-linear relationships, very accurate
- Gradient Boosting (XGBoost)Best accuracy for tabular data like this



# Models  

**XGBoost**  -  for supervised machine learning tasks.
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


----------------------------


**Random Forrest**
-  as an ensemble learning method wherein many decision trees are constructed during training, with the output being either the mean prediction for regression or the mode of the classes for classification. **5 [XGBoost vs. Random Forest vs. Gradient Boosting](https://www.spiceworks.com/soft-tech/xgboost-vs-random-forest-vs-gradient-boosting/)

 - Handles non-linear relationships, very accurate



Features

 

The Good & Bad
Good:
 - Decision trees may be popular supervised learning algorithms but are not immune to problems such as bias and overfitting.


Bad:
 - with multiple decision trees forming an ensemble in Random Forest, more accurate results can be predicted, especially when individual trees are uncorrelated.



