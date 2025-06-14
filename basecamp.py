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


#======================================================using list c
cgpa = []
cutoff = 0.0
print("Enter cgpa of 10 students")
for i in range(10):
    print(f"Student {i+1} cgpa")
    cgpa.append(float(input()))
print("Enter the cut-off cgpa")
cutoff = float(input())

#list comprehension
qualified  = [m for m in cgpa if m >=cutoff]
toppers  = [m for m in cgpa if m >=8.8]


print("Qualified list of cgpa")
print(qualified)
print(toppers)

#========================================================using While True to avoid neg values

sum = 0
n = 0
print("Enter 5 positive numbers")
for i in range(5):
    while True:
        n = int(input())
        if n < 0:
            print("Erorr!!! Neg value entered")
            continue
        sum=sum+n
        break

print(f"Sum of 5 nos is {sum}")
