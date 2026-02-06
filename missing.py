import pandas as pd

# Load CSV
df = pd.read_csv("all_summaries.csv")

# Extract Roll Number column and remove '.csv' if present, convert to integers
df['Roll Number'] = df['Roll Number'].str.replace('.csv','').astype(int)

# Generate expected roll numbers from 1 to 105
expected_rolls = list(range(1, 106))

# Find missing roll numbers
missing_rolls = [r for r in expected_rolls if r not in df['Roll Number'].tolist()]

if missing_rolls:
    print("Missing Roll Numbers:")
    print(missing_rolls)
else:
    print("All Roll Numbers from 01 to 105 are present!")
