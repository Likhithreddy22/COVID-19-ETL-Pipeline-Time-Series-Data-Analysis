import numpy as np
import pandas as pd

def transform(df):
    # Reordering columns
    df = df[['iso_code','location','date','total_cases','new_cases','total_deaths','icu_patients','population']]

    # sorting
    df = df.sort_values(['location','date'])

    # dtype conversion
    df['location'] = df['location'].astype('category')

    # conversion to date time
    df['date'] = pd.to_datetime(df['date'])

    # active cases
    df['active_cases'] = df['total_cases'] - df['total_deaths']

    # handling missing values
    df.fillna(0,inplace = True)

    # handling duplicates
    df.drop_duplicates(inplace = True)

    # creating new column death_rate
    df['death_rate'] = np.where(df['total_cases']>0 , df['total_deaths']/df['total_cases'],0)

    # creating new column
    df['cases_per_million'] = np.where(df['population']>0,df['total_cases']/df['population']*1_000_000,0)

    # finding weekely average
    df['7_day_avg'] = (
        df.groupby('location')['new_cases']
        .transform(lambda x:x.rolling(7).mean())
    )

    return df