employees = { 
    "E001": {"name": "Aarav", "department": "HR", "attendance": ["2025-05-01", "2025-05-02"]},
    "E002": {"name": "Priya", "department": "IT", "attendance": ["2025-05-02"]},
    "E003": {"name": "Ravi", "department": "Finance", "attendance": ["2025-05-01"]},
    "E004": {"name": "Aarav", "department": "Finance", "attendance": ["2025-05-03"]}  # Same name, different ID
}

# Prompt the user to enter the employee ID
emp_id = input("Enter the employee ID (e.g., E001, E002, E003, E004): ")

# Check if the entered ID exists in the dictionary and display the data
if emp_id in employees:
    employee_data = employees[emp_id]
    print(f"Employee ID: {emp_id}")
    print(f"Name: {employee_data['name']}")
    print(f"Department: {employee_data['department']}")
    print(f"Attendance: {', '.join(employee_data['attendance'])}")
else:
    print("Invalid employee ID. Please try again.")
