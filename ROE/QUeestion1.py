import sqlite3
import pandas as pd

conn = sqlite3.connect("retail.db")
df = pd.read_sql_query("SELECT Net_Sales, Promo_Spend, Footfall FROM retail_data", conn)

# Compute all three correlations
print("Net_Sales-Promo_Spend:", df["Net_Sales"].corr(df["Promo_Spend"]))
print("Net_Sales-Footfall:", df["Net_Sales"].corr(df["Footfall"]))
print("Promo_Spend-Footfall:", df["Promo_Spend"].corr(df["Footfall"]))
