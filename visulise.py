import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("all_summaries.csv")

df['MARKS OBTAINED'] = df['MARKS OBTAINED'].str.split('/').str[0].astype(int)

plt.figure(figsize=(18, 7))

sns.barplot(x='Roll Number', y='MARKS OBTAINED', data=df, color='skyblue', label='Marks Obtained')

colors = df['RESULT'].map({'PASS': 'green', 'FAIL': 'red'})
plt.bar(df['Roll Number'], df['CGPA']*100, color=colors, alpha=0.6, label='CGPA (scaled x100)')

plt.plot(df['Roll Number'], df['PERCENTAGE'], color='orange', marker='o', linewidth=1.5, label='Percentage')

plt.xlabel('Roll Number')
plt.ylabel('Marks / CGPA x100 / Percentage')
plt.title('Student Performance: Marks, CGPA, Percentage')

plt.xticks(rotation=110)

plt.legend()

plt.tight_layout()
plt.show()
