from sqlalchemy import create_engine
from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()
user = os.getenv('PG_USER')
password = os.getenv('PG_PASSWORD')
host = os.getenv('PG_HOST')
port = os.getenv('PG_PORT')

def connect_to_raw_db():
    engine_string = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/nobel_raw_data"
    engine = create_engine(engine_string)
    return engine
    
def connect_to_clean_db():
    engine_string = f"postgresql+psycopg2://{user}:{password}@{host}:{port}/nobel_clean_data"
    engine = create_engine(engine_string)   
    return engine