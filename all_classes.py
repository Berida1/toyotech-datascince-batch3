import sqlite3 as sql3
import pandas as pd
import os

# print(sql3.sqlite_version)  

if not os.path.exists("data/processed_data"):
    os.makedirs("data/processed_data")
    
db_path = "data/processed_data/db_analytics.db"
conn = sql3.connect(db_path)

df = pd.DataFrame()
# A new test is here