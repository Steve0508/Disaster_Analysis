import pandas as pd
from sqlalchemy import create_engine
import os

# Change these credentials as per your database setup
DB_USER = 'root'
DB_PASSWORD = '05102004pk'
DB_HOST = 'localhost'
DB_PORT = '3306'
DB_NAME = 'disaster'

# CSV path
CSV_FILE = 'D:\Disaster\dataset\disaster_dataset_ready.csv'

def load_data_to_mysql():
    try:
        # Step 1: Load CSV
        if not os.path.exists(CSV_FILE):
            raise FileNotFoundError(f"CSV file '{CSV_FILE}' not found!")

        df = pd.read_csv(CSV_FILE)

        # Step 2: Connect to MySQL using SQLAlchemy
        engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')

        # Step 3: Load to MySQL (replace existing table if it exists)
        df.to_sql('disasters', con=engine, if_exists='replace', index=False)
        print("✅ Data loaded successfully into 'disasters' table.")
    
    except Exception as e:
        print("❌ Error loading data:", e)

# Run directly if script is executed
if __name__ == "__main__":
    load_data_to_mysql()
