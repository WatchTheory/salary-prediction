

Using Text Columns
- from sklearn.linear_model import LinearRegression
- from sklearn.preprocessing import LabelEncoder


Why Use Encode Text Columns?

- Machine Learning model reqirie numerical input and can't use directly process ( simple terms - Linear regression can't use text and can only use numbers), thus we need to use convert our `job_title` column to numbers. 
  
 
 
 1. Label Encoding 
 - Label Encoding assigns a unique number to each category. In our example, we could assign the number 1 to Poor, 2 to Fair, and so on. So, your list of customer feedback would become [1, 2, 3,4,5]. *1 [Label Encoding vs One-Hot Encoding](https://medium.com/aimonks/label-encoding-vs-one-hot-encoding-making-sense-of-categorical-data-1181914501f3)
 
 
Pros  - Good with Order like "low", "Medium", "High"
Label Encoding is great when you have categories with an inherent order or rank, like ‘low,’ ‘medium,’ and ‘high’ in a survey response. However, it has a drawback when used for nominal categories, such as colors, because it can imply an unintended order. *2 [Label Encoding vs One-Hot Encoding](https://medium.com/aimonks/label-encoding-vs-one-hot-encoding-making-sense-of-categorical-data-1181914501f3)






2. One-Hot Encoding
One-hot encoding is a method of converting categorical variables into a format that can be provided to machine learning algorithms to improve prediction. It involves creating new binary columns for each unique category in a feature. Each column represents one unique category, and a value of 1 or 0 indicates the presence or absence of that category. *3 [What Is One Hot Encoding and How to Implement It in Python](https://www.datacamp.com/tutorial/one-hot-encoding-python-tutorial) 

Pros - transform categorical data [Text data] into a seperate column to be used for on a machine learning Model


For example, assigning 1 to Red, 2 to Green, and 3 to Blue could make the model think that Green is greater than Red and Blue is greater than both. This misunderstanding can negatively affect the model's performance.One-hot encoding solves this problem by creating a separate binary column for each category. This way, the model can see that each category is distinct and unrelated to the others. 



Best Practices & Considerations

- Hot-Encoding in Scikit-leanr [One Hot Encoding Using Scikit-Learn](https://builtin.com/articles/one-hot-encoding)
- Hot-Encoding in Pandas [One Hot Encoding in Pandas](https://builtin.com/articles/one-hot-encoding)


Using the “raw” version of OneHotEncoder, i.e. without a column transformer, needs the most manual adjustment, and I only see rare cases in which I would use this approach in practice.
If your process relies on scikit pipelines, which has many advantages, then using scikit OneHotEncoder with a column transformer seems to be the most natural choice to me.
If you like to process the data step-by-step, going from DataFrame to DataFrame, which can be a good choice in the exploration phase, then I would definitely take the pandas.get_dummies approach.




## What Machine Learning Model to use 

- Random ForestHandles non-linear relationships, very accurate
- Gradient Boosting (XGBoost)Best accuracy for tabular data like this





