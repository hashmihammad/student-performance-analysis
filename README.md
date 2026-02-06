# Student Performance Analysis

## Project Overview
This project analyzes and visualizes student performance data, including **Marks Obtained, CGPA, and Percentage**.  
The main goal is to explore trends, summarize overall performance, and provide insights on student outcomes.

> ⚠️ **Privacy Note:** Scripts used to automate data collection are **not included** for security reasons. Only processed data and visualization code are shared.

---

## Data Collection
- Data was **automatically extracted** from the [University of Sindh Transcript Portal](https://exam.usindh.edu.pk/v2/trancript.php).  
- Automation was performed using Python (libraries used included `selenium`, `csv`, and `re`), but the scripts are **not shared**.  
- Individual CSV files were collected for each student and then combined into **`all_summaries.csv`**, which contains anonymized student performance summaries.  

- **Missing Roll Numbers:**  
  Some roll numbers could not be extracted automatically. These are listed in `missing.py`. No manual entry was performed—all data comes from the automated process.

---

## Repository Contents
- `visulise.py` – Python script for visualizing student performance  
- `all_summaries.csv` – Processed dataset with anonymized student performance data  

> Other scripts such as `main.py`, `cgpa.py`, and `missing.py` are **not included** to maintain privacy and security.

---

## Visualization
The `visulise.py` script generates the following charts:
- **Marks Obtained** (bar chart)  
- **CGPA comparison** (scaled ×100) with color coding:  
  - Green = PASS  
  - Red = FAIL  
- **Percentage** (line chart)  
- X-axis: Roll Number  
- Y-axis: Marks / CGPA ×100 / Percentage  

**Example Output:**  
*(Add a screenshot of your chart here if desired)*

---

## How to Run
1. Install Python ≥ 3.8  
2. Install required libraries:
```bash
pip install pandas matplotlib seaborn
````

3. Run the visualization:

```bash
python visulise.py
```

4. A plot will display student performance trends.

---

## Notes

* Only anonymized data is included in `all_summaries.csv`.
* `missing.py` lists roll numbers whose data could not be extracted automatically.
* This project demonstrates **data collection, processing, and visualization** while maintaining privacy and security.
