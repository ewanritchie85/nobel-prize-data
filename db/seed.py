import pandas as pd
from utils.db_connection import connect_to_db
from utils.extract_utils import create_df_from_json


# no longer appropriate
def seed_db(data):
    table_name = data[1]
    table_columns = data[2]
    df = data[0]
    
    engine = connect_to_db()
    
    df.to_sql(table_name, engine, if_exists='replace', index=False)
    
    
    
    