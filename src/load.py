from sqlalchemy import create_engine
from config.config import DB_URI,Processed_Data

def load_to_db(df):
    engine = create_engine(DB_URI)
    df.to_sql('covid_data',engine,if_exists = 'replace', index = False)

def save_to_csv(df):
    import os
    print("Saving to:", os.path.abspath(Processed_Data))
    df.to_csv(Processed_Data,index = False)
