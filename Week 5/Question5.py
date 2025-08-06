import pandas as pd

DATA_PATH = "q-clean-up-sales-data.json"

try:
    df = pd.read_json(DATA_PATH)
except ValueError:
    df = pd.read_json(DATA_PATH, lines=True)

df_filtered = df[
    (df["product"].str.strip().str.lower() == "bike") &
    (df["sales"] >= 97)
].copy()

print("Filtered records:", len(df_filtered))

# Clean city names thoroughly
df_filtered["city_clean"] = (
    df_filtered["city"]
    .str.strip()
    .str.replace(r"\s+", " ", regex=True)
    .str.lower()
)

# Map all Dhaka variants to 'dhaka'
df_filtered["city_clean"] = df_filtered["city_clean"].replace({
    "dhaka": "dhaka",
    "dhacka": "dhaka",
    "daka": "dhaka",
    "dhaaka": "dhaka",
    "dhakaa": "dhaka"
})

# Group by cleaned city
summary = (
    df_filtered
    .groupby("city_clean")["sales"]
    .sum()
    .reset_index()
)

print("\nAggregated sales per city:")
print(summary)

# Retrieve Dhaka
dhaka_sales = summary.loc[
    summary["city_clean"] == "dhaka",
    "sales"
]

if not dhaka_sales.empty:
    total_units = int(dhaka_sales.iloc[0])
    print(f"\n✅ Total units sold in Dhaka: {total_units}")
else:
    print("\n⚠️ No matching records for Dhaka.")
