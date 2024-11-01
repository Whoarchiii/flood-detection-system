# src/preprocess.py
import pandas as pd

def preprocess_data(data):
    """Clean and preprocess the data."""
    data['Date'] = pd.to_datetime(data['Date'], errors='coerce')
    data['Rainfall (cm)'] = pd.to_numeric(data['Rainfall (cm)'], errors='coerce')
    data.dropna(subset=['Date', 'Rainfall (cm)'], inplace=True)
    return data
