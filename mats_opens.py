import pandas as pd
from pathlib import Path

short_open = 1.5272
long_open = 48.662

FILE = "ticker_data_log/mats_logs_opens.csv"

if not Path(FILE).exists():
    df = pd.DataFrame(columns=[
        "datum",
        "long_open",
        "short_open"
    ])
    df.to_csv(FILE, index=False)

# Nieuwe rij
new_date = "2026-05-29"

new_row = {
    "datum": new_date,
    "long_open": long_open,
    "short_open": short_open
}

# Bestaande data laden
df = pd.read_csv(FILE)

# Check of datum al bestaat
if (df["datum"] == new_date).any():
    raise ValueError(f"Datum {new_date} bestaat al in {FILE}")

# Toevoegen
pd.DataFrame([new_row]).to_csv(
    FILE,
    mode="a",
    header=False,
    index=False
)

print("Rij toegevoegd.")
