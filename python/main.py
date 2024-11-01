# main.py
from src.data_loader import load_data
from src.preprocess import preprocess_data
print("Module imported successfully")
from src.flood_risk import analyze_flood_risk
from config.settings import RAINFALL_THRESHOLD

# Load data
data = load_data()
if data is not None:
    # Preprocess data
    data = preprocess_data(data)

    # Analyze flood risk
    results = analyze_flood_risk(data, RAINFALL_THRESHOLD)

    # Display results
    print("\nPotential Flood Risk Entries (Rainfall > 20 cm):\n", results["flood_risk_data"][['Date', 'Station', 'Met. Subdivision', 'Rainfall (cm)']])
    print("\nNumber of High-Risk Entries per Subdivision:\n", results["risk_counts"])
    print(f"\nSummary:\nTotal entries analyzed: {results['total_entries']}")
    print(f"Total high-risk entries (Rainfall > {RAINFALL_THRESHOLD} cm): {results['high_risk_entries']}")
    print("High-risk subdivisions:", results["high_risk_subdivisions"])
