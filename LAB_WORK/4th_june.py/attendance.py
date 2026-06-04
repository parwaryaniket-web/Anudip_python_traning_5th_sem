 ## a teacher recording student attendence class of 30 students,every time we need to insert student is present or absent,
#count total no. of students present and absent, then calculate percentage of students present and absent.
print("-----ATTENDANCE COUNTER-----")

total_students = 30
present = 0
absent = 0

for i in range(total_students):
    status = input("Is student", i+1, "present? (y/n): ")

    if status == "y":
        present += 1
    else:
        absent += 1

percentage_present = (present / total_students) * 100
percentage_absent = (absent / total_students) * 100

print("\nTotal students:", total_students)
print("Present:", present)
print("Absent:", absent)
print("Percentage present:", round(percentage_present, 2), "%")
print("Percentage absent:", round(percentage_absent, 2), "%")






