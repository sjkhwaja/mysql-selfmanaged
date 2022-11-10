### Import packages
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
import os

load_dotenv()

# Define login Creds
mysql_host = os.getenv('MYSQL_HOSTNAME')
mysql_user = os.getenv('MYSQL_USERNAME')
mysql_pwd = os.getenv('MYSQL_PASSWORD')
mysql_db = os.getenv('MYSQL_DATABASE')

# Connection string
connection = f'mysql+pymysql://{mysql_user}:{mysql_pwd}@{mysql_host}/{mysql_db}'
db = create_engine(connection)

# Define query
query = 'SELECT & FROM db1.table1;'
query
df = pd.read_sql(query, con=db) # error; update default settings. MYSQL config to allow internal connections and VM config for port 3306


# Create df
real_df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/HHA-507-2022/main/descriptive/example1/data/data.csv')
real_df

# Push df to new db
real_df.to_sql('table1', con=db, if_exists='replace')
