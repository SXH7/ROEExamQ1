import re

# File path
DATA_PATH = "q-parse-partial-json.jsonl"

# Compile regex to extract 'sales' value
# Matches: "sales":115 or "sales": 115
sales_pattern = re.compile(r'"sales"\s*:\s*(\d+)')

# Initialize total
total_sales = 0
count = 0

with open(DATA_PATH, "r", encoding="utf-8") as f:
    for i, line in enumerate(f, start=1):
        line = line.strip()
        if not line:
            continue

        # Search for sales
        match = sales_pattern.search(line)
        if match:
            value = int(match.group(1))
            total_sales += value
            count += 1
        else:
            print(f"Line {i}: No sales value found")

print(f"\nProcessed {count} records with sales.")
print(f"Total sales value: {total_sales}")
