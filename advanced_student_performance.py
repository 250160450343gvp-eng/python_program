TOTAL_STUDENTS = 10
subject_names = ("Sub1", "Sub2", "Sub3", "Sub4", "Sub5") 
students_data = []  
sen_name = set()
duplicate_name = []

print("=========================")
print("  ENTER DETAILS FOR 10 STUDENTS  ")
print("=========================")

for i in range(1, TOTAL_STUDENTS + 1):
    print(f"\n--- Student {i} ---")
    roll_no = input("Enter Roll Number: ")
    name = input("Enter Name: ")

    if name in sen_name:
        duplicate_name.append(name)
    else:
        sen_name.add(name)

    marks_list = []
    for sub in subject_names:
        m = float(input(f"Enter marks for {sub}: "))
        marks_list.append(m)
    marks_tuple = tuple(marks_list)
    student_dict = {
        "roll": roll_no,
        "name": name,
        "marks": marks_tuple
    }
    students_data.append(student_dict)
all_percentages = []

for student in students_data:
    total = sum(student["marks"])
    percentage = total / 5.0

    if percentage >= 85:
        grade = 'A'
    elif percentage >= 70:
        grade = 'B'
    elif percentage >= 55:
        grade = 'C'
    elif percentage >= 40:
        grade = 'D'
    else:
        grade = 'F'

    student["total"] = total
    student["percentage"] = percentage
    student["grade"] = grade

    all_percentages.append(percentage)
class_avg_percentage = sum(all_percentages) / TOTAL_STUDENTS

highest_perc = max(all_percentages)
lowest_perc = min(all_percentages)

highest_scorers = [s["name"] for s in students_data if s["percentage"] == highest_perc]
lowest_scorers = [s["name"] for s in students_data if s["percentage"] == lowest_perc]

second_highest_perc = -1
for p in all_percentages:
    if p < highest_perc and p > second_highest_perc:
        second_highest_perc = p

second_highest_scorers = [s["name"] for s in students_data if s["percentage"] == second_highest_perc]

above_avg_students = [s["name"] for s in students_data if s["percentage"] > class_avg_percentage]

failed_students = []
for s in students_data:
    has_failed = False
    for mark in s["marks"]:
        if mark < 40:
            has_failed = True
            break
    if has_failed:
        failed_students.append(s["name"])

subject_totals = [0.0, 0.0, 0.0, 0.0, 0.0]
for s in students_data:
    for index in range(5):
        subject_totals[index] += s["marks"][index]

subject_averages = [t / TOTAL_STUDENTS for t in subject_totals]
highest_sub_avg = max(subject_averages)
best_sub_index = subject_averages.index(highest_sub_avg)
best_subject = subject_names[best_sub_index]

grade_dict = {"A": [], "B": [], "C": [], "D": [], "F": []}
for s in students_data:
    grade_dict[s["grade"]].append(s["name"])

all_names = [s["name"] for s in students_data]
alphabetical_names = sorted(all_names)

print("\n==========================")
print(" STUDENT PERFORMANCE ANALYTICS REPORT")
print("============================")
print(f"\n1. Class Average Percentage : {class_avg_percentage:.2f}%")
print(f"\n2. Highest Scorer(s) : {', '.join(highest_scorers)} ({highest_perc:.2f}%)")
print(f"3. Lowest Scorer(s): {', '.join(lowest_scorers)} ({lowest_perc:.2f}%)")

if second_highest_perc != -1:
    print(f"4. Second-Highest Scorer(s) : {', '.join(second_highest_scorers)} ({second_highest_perc:.2f}%)")
else:
    print("4. Second-Highest Scorer(s) : None (All students scored the same)")

print(f"\n5. Subject with Highest Avg : {best_subject} ({highest_sub_avg:.2f} avg marks)")

print("\n6. Students Scoring Above Class Average:")
for name in above_avg_students:
    print(f"•{name}")

print("\n7. Students Failed in One or More Subjects (< 40 marks):")
if failed_students:
    for name in failed_students:
        print(f"•{name}")

else:
    print("None (All students passed all subjects)")

print("\n8. Grade Distribution Dictionary:")
for g, names in grade_dict.items():
    print(f" Grade '{g}' : {names}")

print("\n9. Names in Alphabetical Order (Original Data Untouched):")
print(f"{alphabetical_names}")

print("\n10. Duplicate Names Report:")
if duplicate_name:
    print(f"Duplicate entries detected: {set(duplicate_name)}")
else:
    print("No duplicate student names found.")