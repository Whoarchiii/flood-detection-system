# config/settings.py
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'test.xls')
RAINFALL_THRESHOLD = 20  # Threshold for potential flood risk (cm)