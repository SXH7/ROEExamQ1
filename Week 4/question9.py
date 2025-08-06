from PyPDF2 import PdfReader, PdfWriter
import pandas as pd
import re

# Step 1: Extract Pages 62–97 from the PDF
reader = PdfReader("Week 4\q-extract-tables-from-pdf.pdf")
writer = PdfWriter()

for i in range(61, 97):  # zero-indexed (61 = page 62)
    writer.add_page(reader.pages[i])

with open("pages_62_97.pdf", "wb") as f:
    writer.write(f)

# Step 2: Extract Text From Extracted Pages
extracted_text = ""
for page in PdfReader("pages_62_97.pdf").pages:
    extracted_text += page.extract_text() + "\n"

# Step 3: Use Regex to Extract Rows of Marks
pattern = r"(\d{1,3})\s+(\d{1,3})\s+(\d{1,3})\s+(\d{1,3})\s+(\d{1,3})"
matches = re.findall(pattern, extracted_text)

# Step 4: Convert to DataFrame
df = pd.DataFrame(matches, columns=["Maths", "Physics", "English", "Economics", "Biology"])
df = df.astype(int)

# Step 5: Filter and Calculate Total
filtered_df = df[df["Maths"] >= 49]
total_physics = filtered_df["Physics"].sum()

print("Total Physics marks (Maths ≥ 49, pages 62–97):", total_physics)
