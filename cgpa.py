import csv
import os

# Path containing all individual CSVs
input_folder = r"E:\My Projects\PythonProject2\PythonProject\My_20_Projects"
# Output file
output_file = r"/student marks visulisation/all_summaries.csv"

# Keys we want to extract
summary_keys = ["MARKS OBTAINED", "CGPA", "RESULT", "PERCENTAGE"]

# Prepare list to hold all rows
all_rows = []

# Loop through all CSV files in folder
for filename in os.listdir(input_folder):
    if filename.endswith(".csv"):
        file_path = os.path.join(input_folder, filename)
        summary_values = []
        with open(file_path, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if row and row[0] in summary_keys:
                    summary_values.append(row[1])
        if summary_values:  # Only add if we found summary
            all_rows.append([filename] + summary_values)  # Add filename for reference

# Write combined CSV
with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Roll Number"] + summary_keys)  # Header row
    writer.writerows(all_rows)

print(f"All summaries saved to {output_file}")
