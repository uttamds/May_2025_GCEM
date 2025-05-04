# 1. Dictionary to store employee info with unique IDs
employees = {
    "E001": {"name": "Alice", "department": "HR", "attendance": ["2025-05-01", "2025-05-02"]},
    "E002": {"name": "Bob", "department": "IT", "attendance": ["2025-05-02"]},
    "E003": {"name": "Charlie", "department": "Finance", "attendance": ["2025-05-01"]},
    "E004": {"name": "Alice", "department": "Finance", "attendance": ["2025-05-03"]}  # Same name, different ID
}

# 2. Add a new attendance entry for Bob (E002)
employees["E002"]["attendance"].append("2025-05-03")

# 3. Print attendance for Bob
print("Updated Attendance for Bob (E002):", employees["E002"]["attendance"])

# 4. List all unique departments
departments = {info["department"] for info in employees.values()}
print("Departments:", departments)

# 5. Find all employees named 'Alice'
alices = [emp_id for emp_id, info in employees.items() if info["name"] == "Alice"]
print("Employees named Alice:", alices)

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
