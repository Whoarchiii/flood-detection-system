# src/data_loader.py
import pandas as pd
from config.settings import DATA_PATH

def load_data():
    """Load data from an Excel file."""
    try:
        data = pd.read_excel(DATA_PATH)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
