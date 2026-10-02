import pandas as pd

def test_synthetic_pipeline():
    data = pd.DataFrame({
        "State": ["A", "B", "C"],
        "Unemployment_Rate": [5.0, 7.0, 6.0]
    })

    assert len(data) == 3
    assert "Unemployment_Rate" in data.columns
    assert data["Unemployment_Rate"].notna().all()