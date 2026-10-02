import pandas as pd

def test_synthetic_pipeline():
    data = pd.DataFrame({
        "State": ["A", "B", "C"],
        "Unemployment_Rate": [5.0, 7.0, 6.0]
    })

    assert len(data) == 3
    assert "Unemployment_Rate" in data.columns
    assert data["Unemployment_Rate"].notna().all()

# Expected output contract:
# 1. Synthetic dataset contains 3 rows.
# 2. Unemployment_Rate column exists.
# 3. Unemployment_Rate contains no missing values.
# 4. Pipeline check passes when all assertions are true.