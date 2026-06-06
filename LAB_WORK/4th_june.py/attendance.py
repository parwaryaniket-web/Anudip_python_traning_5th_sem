 ## a teacher recording student attendence class of 30 students,every time we need to insert student is present or absent,
#count total no. of students present and absent, then calculate percentage of students present and absent.
print("-----ATTENDANCE COUNTER-----")

total_students = 30
present = 0
absent = 0

for i in range(total_students):# Loop through each student
    status = input("Is student", i+1, "present? (y/n): ")# Get the attendance status for each student

    if status == "y":# If the student is present, increment the present count
        present += 1# If the student is absent, increment the absent count
    else:# If the student is absent, increment the absent count
        absent += 1# Calculate the percentage of students present and absent

percentage_present = (present / total_students) * 100# Calculate the percentage of students present
percentage_absent = (absent / total_students) * 100# Calculate the percentage of students absent

print("\nTotal students:", total_students)# Print the total number of students
print("Present:", present)
print("Absent:", absent)
print("Percentage present:", round(percentage_present, 2), "%")# Print the percentage of students present, rounded to 2 decimal places
print("Percentage absent:", round(percentage_absent, 2), "%")# Print the percentage of students absent, rounded to 2 decimal places






