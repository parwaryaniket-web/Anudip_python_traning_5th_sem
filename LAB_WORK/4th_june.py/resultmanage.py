#6. Student Result Management System 
#Accept marks of 5 subjects. 
#Display
#Total Marks
#Average Marks  
#Percentage
#Grade (A, B, C, D, F) based on percentage
print("-----STUDENT RESULT MANAGEMENT SYSTEM-----")
subjects = 5
marks = []  
for i in range(subjects):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)  
total_marks = sum(marks)
average_marks = total_marks / subjects
percentage = (total_marks / (subjects * 100)) * 100

if percentage >= 80:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average_marks}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")