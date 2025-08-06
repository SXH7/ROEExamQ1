import pandas as pd

url = "https://stats.espncricinfo.com/ci/engine/stats/index.html?class=2;template=results;type=batting;page=8"

# Read all tables from the page
tables = pd.read_html(url)

# ODI batting stats is the first table
df = tables[0]

# The "0" column contains duck counts
if "0" in df.columns:
    total_ducks = df["0"].sum()
    print("Total ducks on page 8:", total_ducks)
else:
    print("Column '0' not found")
