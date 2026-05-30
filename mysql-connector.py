import mysql.connector
from mysql.connector import Error
import pandas as pd
from sqlalchemy import create_engine


def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password)
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"MySQL: {e}")
    return connection




# 1. Define connection string (replace with your credentials)
# Format: mysql+driver://username:password@host:port/database_name
# engine = create_engine("mysql+pymysql://user:password@localhost/mydb")
engine = create_engine("mysql+pymysql://root:black@localhost/resume")

# 2. Use pandas dataframe to insert data into MySQL

# read csv file into pandas dataframe
df_data = pd.read_csv("Cleaned_Salary_Data.csv")


# 3. Insert DataFrame into MySQL
# if_exists='append' adds to existing table; 'replace' drops and recreates it
df_data.to_sql(
     name='resume',
     con=engine,
     if_exists='append',
     index=False            # Set to False to avoid writing data index column to Mysql
)



# df.to_sql(
#     name='my_table',       # Table name
#     con=engine,            # SQLAlchemy engine
#     if_exists='append',    # 'append', 'replace', or 'fail'
#     index=False            # Do not write DataFrame index to DB
# )