student_record = {}  #dictionary.
print("Enter stud data")
while True:
    try:
        student_record['name'] = input("Enter name")
        student_record['age'] = int(input("Enter age"))
        student_record['roll'] = int(input("Enter roll"))
        student_record['phone'] = input("Enter phone")
    except:
        print("Error! please enter only numerics for age, roll")
        print("Enter the data all over again...")
        continue
    print(student_record)
    break

if student_record['age'] <18:
    print("The student is a minor")
else:
    print("Student is adult")