from sqlalchemy import create_engine, text
import pandas as pd
import matplotlib.pyplot as plt
from config.config import DB_URI

def top_10_countries_cases():

    engine = create_engine(DB_URI)

    query = """
    SELECT location, MAX(total_cases) as max_cases
    FROM covid_data
    GROUP BY location
    ORDER BY max_cases DESC
    LIMIT 10
    """

    with engine.connect() as conn:
        df = pd.read_sql(text(query), conn)

    plt.figure(figsize=(10,5))
    plt.bar(df["location"], df["max_cases"])
    plt.xticks(rotation=45)
    plt.title("Top 10 Countries by COVID Cases")
    plt.tight_layout()
    plt.show()