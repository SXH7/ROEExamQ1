import json

def count_key_occurrences(obj, target_key):
    count = 0
    if isinstance(obj, dict):
        for key, value in obj.items():
            if key == target_key:
                count += 1
            # Recursively check the value
            count += count_key_occurrences(value, target_key)
    elif isinstance(obj, list):
        for item in obj:
            count += count_key_occurrences(item, target_key)
    return count

# Path to your JSON log file
json_file_path = "q-extract-nested-json-keys.json"

# Load JSON data
with open(json_file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

# Count occurrences of the key 'WXMX'
target_key = "WXMX"
total_occurrences = count_key_occurrences(data, target_key)

print(f"Total occurrences of key '{target_key}': {total_occurrences}")
