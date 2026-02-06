from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import csv
import re

# --- Step 1: Setup Chrome ---
chrome_options = Options()
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--window-size=1920,1080")

service = Service("E:/Youtube/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=chrome_options)

# --- Step 2: Open transcript page ---
driver.get("https://exam.usindh.edu.pk/v2/trancript.php")
time.sleep(2)

# --- Step 3: Fill form ---
roll_number = "2K23/DS/97"
driver.find_element(By.ID, "roll_no").send_keys(roll_number)

part_dropdown = Select(driver.find_element(By.ID, "part"))
part_dropdown.select_by_visible_text("I")

year_dropdown = Select(driver.find_element(By.ID, "exam_year"))
year_dropdown.select_by_visible_text("2024")

driver.find_element(By.ID, "display").click()
time.sleep(5)  # wait for page to load fully

# --- Step 4: Extract Transcript ---
transcript_div = driver.find_element(By.ID, "Transcript")
transcript_text = transcript_div.text

driver.quit()  # close browser

# --- Step 5: Parse Student Info ---
student_info = {}
student_info_patterns = {
    "NAME": r"NAME:\s*(.+)",
    "FATHER'S NAME": r"FATHER'S NAME:\s*(.+)",
    "SURNAME": r"SURNAME:\s*(.+)",
    "ROLL NO": r"ROLL NO:\s*(.+)"
}

for key, pattern in student_info_patterns.items():
    match = re.search(pattern, transcript_text)
    if match:
        student_info[key] = match.group(1).strip()

# --- Step 6: Parse Courses ---
courses = []
current_semester = None
for line in transcript_text.splitlines():
    line = line.strip()
    # Detect semester header
    sem_match = re.match(r"(FIRST|SECOND|THIRD|FOURTH|FIFTH|SIXTH|SEVENTH|EIGHTH) SEMESTER", line)
    if sem_match:
        current_semester = sem_match.group(0)
        continue

    # Detect course rows (Course No starts with letters)
    course_match = re.match(r"([A-Z]+\d+)\s+(.+?)\s+(\d+)\s+(\d+)\s+(\d+)\s+([A-F][+-]?)\s+([\d.]+)", line)
    if course_match and current_semester:
        course = {
            "Semester": current_semester,
            "Course No": course_match.group(1),
            "Subject": course_match.group(2),
            "Max Marks": course_match.group(3),
            "Min Marks": course_match.group(4),
            "Obt Marks": course_match.group(5),
            "Grade": course_match.group(6),
            "Q.P": course_match.group(7)
        }
        courses.append(course)

# --- Step 7: Parse Overall Summary ---
summary = {}
summary_patterns = {
    "MARKS OBTAINED": r"MARKS OBTAINED:\s*(.+)",
    "CGPA": r"CGPA:\s*(.+)",
    "RESULT": r"RESULT:\s*(.+)",
    "PERCENTAGE": r"PERCENTAGE:\s*(.+)",
    "RESULT DECLARED": r"RESULT DECLARED:\s*(.+)"
}

for key, pattern in summary_patterns.items():
    match = re.search(pattern, transcript_text)
    if match:
        summary[key] = match.group(1).strip()

# --- Step 8: Save to CSV ---
with open("marksheet.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)

    # Write student info
    writer.writerow(["Student Info"])
    for k, v in student_info.items():
        writer.writerow([k, v])
    writer.writerow([])

    # Write courses
    writer.writerow(["Semester", "Course No", "Subject", "Max Marks", "Min Marks", "Obt Marks", "Grade", "Q.P"])
    for course in courses:
        writer.writerow([
            course["Semester"], course["Course No"], course["Subject"], course["Max Marks"],
            course["Min Marks"], course["Obt Marks"], course["Grade"], course["Q.P"]
        ])
    writer.writerow([])

    # Write summary
    writer.writerow(["Summary"])
    for k, v in summary.items():
        writer.writerow([k, v])

print("Transcript data saved to marksheet.csv")
