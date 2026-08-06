
total_students = int(input("Enter number of students: "))

students_data = []


print("\n--- Enter Student Details ---")
for i in range(1, total_students + 1):
    name = input(f"Enter name for student {i}: ")
    marks = float(input(f"Enter marks for {name}: "))
    students_data.append((name, marks))

marks_list = [marks for name, marks in students_data]
marks_tuple = tuple(marks_list)
unique_marks = set(marks_tuple)
student_dict = {name: marks for name, marks in students_data}

highest_marks = max(marks_tuple)
lowest_marks = min(marks_tuple)
average_marks = sum(marks_tuple) / len(marks_tuple)

print("\n===========")
print("STUDENT MARKS ANALYSIS ")
print("=============")

print(f"1. Marks List: {marks_list}")
print(f"2. Marks Tuple: {marks_tuple}")
print(f"3. Unique Marks: {unique_marks}")

print("\n------- Statistics -------")
print(f"• Highest Marks: {highest_marks}")
print(f"• Lowest Marks : {lowest_marks}")
print(f"• Average Marks: {average_marks:.2f}")

print("\n------ Students Above Average -------")
for name, score in student_dict.items():
    if score > average_marks:
        print(f"• {name} : {score}")
print("=====================")