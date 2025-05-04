# 1. Dictionary to store employee info with unique IDs
employees = {
    "E001": {"name": "Aarav", "department": "HR", "attendance": ["2025-05-01", "2025-05-02"]},
    "E002": {"name": "Priya", "department": "IT", "attendance": ["2025-05-02"]},
    "E003": {"name": "Ravi", "department": "Finance", "attendance": ["2025-05-01"]},
    "E004": {"name": "Aarav", "department": "Finance", "attendance": ["2025-05-03"]}  # Same name, different ID
}

# 2. Add a new attendance entry for Priya (E002)
employees["E002"]["attendance"].append("2025-05-03")

# 3. Print attendance for Priya
print("Updated Attendance for Priya (E002):", employees["E002"]["attendance"])

# 4. List all unique departments
departments = {info["department"] for info in employees.values()}
print("Departments:", departments)

# 5. Find all employees named 'Aarav'
aaravs = [emp_id for emp_id, info in employees.items() if info["name"] == "Aarav"]
print("Employees named Aarav:", aaravs)

# 6. Find all employees present on '2025-05-02'
present_on_may2 = [
    info["name"] + " (" + emp_id + ")"
    for emp_id, info in employees.items()
    if "2025-05-02" in info["attendance"]
]
print("Employees present on 2025-05-02:", present_on_may2)

# 7. Define a fixed list of company holidays using a tuple
holidays = ("2025-05-01", "2025-12-25")
print("Company Holidays:", holidays)
