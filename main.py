from src.extract import extract
from src.transform import transform
from src.load import save_to_csv ,load_to_db
from src.analysis import top_10_countries_cases

def run():

    print("Starting pipeline...")

    df = extract()
    print("Data extracted")

    df = transform(df)
    print("Data transformed")

    save_to_csv(df)
    print("CSV saved")

    load_to_db(df)
    print("Data loaded to database")

    top_10_countries_cases()
    print("Analysis completed")
    
if __name__ == "__main__":
    run()
