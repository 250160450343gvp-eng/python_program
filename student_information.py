
n = int(input("Enter total number of students: "))

for i in range(1, n + 1):
    print(f"\n======== Enter Details for Student {i} ======")
    roll_no = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    marks1 = int(input("Enter marks of Subject 1: "))
    marks2 = int(input("Enter marks of Subject 2: "))
    marks3 = int(input("Enter marks of Subject 3: "))
    
    total = marks1 + marks2 + marks3
    percentage = total / 3.0
    
    if marks1 >= 40 and marks2 >= 40 and marks3 >= 40:
        result = "PASS"
    else:
        result = "FAIL"

    print("\n+----------------+----------------+")
    print("| -----------Personal Details-----+")
    print(f"| Roll No        | {roll_no}")
    print(f"| Name           | {name}")
    print(f"| Age            | {age}")
    print("+----------------+----------------+")
    print("| -----Subject & Marks Details----+")
    print(f"| Subject 1      | {marks1}")
    print(f"| Subject 2      | {marks2}")
    print(f"| Subject 3      | {marks3}")
    print("+----------------+----------------+")
    print("| -----------Result Details-------+")
    print(f"| Total Marks    | {total}")
    print(f"| Percentage     | {percentage:.2f}%")
    print(f"| Result         | {result}")
    print("+----------------+----------------+")
    print(" Minimum 40 marks are required in each subject\n")
    