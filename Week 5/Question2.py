import re

DATA_PATH = "q-clean-up-student-marks.txt"

unique_ids = set()

with open(DATA_PATH, "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        
        # Split by dash; take the last segment (the ID part)
        parts = line.split("-")
        if len(parts) < 2:
            print(f"Skipping line (no dash): {line}")
            continue
        
        id_part = parts[-1].strip()
        
        # Remove 'Marks' or ':Marks' or '::Marks' (case insensitive), with optional spaces
        id_clean = re.sub(r'[:]*\s*Marks.*$', '', id_part, flags=re.IGNORECASE).strip()
        
        # Remove any leading/trailing punctuation
        id_clean = id_clean.strip(":").strip()
        
        if id_clean:
            unique_ids.add(id_clean)
        else:
            print(f"Could not extract ID from line: {line}")

print(f"\nTotal unique students: {len(unique_ids)}")
