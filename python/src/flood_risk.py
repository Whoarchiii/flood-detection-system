# src/flood_risk.py
def analyze_flood_risk(data, threshold):
    """Analyze flood risk based on rainfall threshold."""
    flood_risk_data = data[data['Rainfall (cm)'] > threshold]
    risk_counts = flood_risk_data['Met. Subdivision'].value_counts()
    
    return {
        "flood_risk_data": flood_risk_data,
        "risk_counts": risk_counts,
        "total_entries": len(data),
        "high_risk_entries": len(flood_risk_data),
        "high_risk_subdivisions": risk_counts.index.tolist(),
    }
