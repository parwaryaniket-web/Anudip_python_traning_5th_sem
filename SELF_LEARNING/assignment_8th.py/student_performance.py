'''
1. Student Performance Analytics System 
Problem Statement 
A coaching institute wants to analyze student performance. 
Store details of at least 30 students in a dictionary. 
Example Structure 
students = { 
    "S101": {"name": "Anuj", "marks": 85}, 
    "S102": {"name": "Rahul", "marks": 72} 
} 
Requirements 
1. Display all student records.  
2. Search a student using Student ID.  
3. Add a new student.  
4. Update marks of an existing student.  
5. Delete a student.  
6. Find topper and lowest scorer.  
7. Calculate class average.  
8. Count pass and fail students.  
9. Generate grades:  
o A (90+)  
o B (75–89)  
o C (50–74)  
o F (<50)  
10. Display students scoring above average.  
11. Display top 5 performers.  
12. Create a separate dictionary for scholarship students (marks > 85).  
Expected Learning 
• Nested Dictionaries  
• Dictionary Traversal  
• Searching  
• Aggregation  
• Report Generation  
'''
# Student Performance Analytics System

# Dictionary containing details of 30 students
students = {
    "S101":{"name":"Anuj","marks":85},
    "S102":{"name":"Rahul","marks":72},
    "S103":{"name":"Priya","marks":91},
    "S104":{"name":"Karan","marks":45},
    "S105":{"name":"Neha","marks":67},
    "S106":{"name":"Amit","marks":88},
    "S107":{"name":"Pooja","marks":76},
    "S108":{"name":"Rohit","marks":54},
    "S109":{"name":"Simran","marks":95},
    "S110":{"name":"Arjun","marks":39},
    "S111":{"name":"Riya","marks":82},
    "S112":{"name":"Vikas","marks":70},
    "S113":{"name":"Sneha","marks":60},
    "S114":{"name":"Manish","marks":47},
    "S115":{"name":"Asha","marks":93},
    "S116":{"name":"Deepak","marks":79},
    "S117":{"name":"Nisha","marks":68},
    "S118":{"name":"Varun","marks":51},
    "S119":{"name":"Komal","marks":86},
    "S120":{"name":"Yash","marks":74},
    "S121":{"name":"Payal","marks":90},
    "S122":{"name":"Akash","marks":55},
    "S123":{"name":"Meena","marks":48},
    "S124":{"name":"Sanjay","marks":83},
    "S125":{"name":"Divya","marks":97},
    "S126":{"name":"Mohit","marks":62},
    "S127":{"name":"Tina","marks":78},
    "S128":{"name":"Raj","marks":43},
    "S129":{"name":"Kriti","marks":89},
    "S130":{"name":"Harsh","marks":58}
}

# -------------------------------------------------
# 1. Display all student records
# -------------------------------------------------
print("ALL STUDENT RECORDS")

for sid, data in students.items():
    print(sid, data)

# -------------------------------------------------
# 2. Search a student using Student ID
# -------------------------------------------------
sid = input("\nEnter Student ID to Search: ")

if sid in students:
    print("Student Found:", students[sid])
else:
    print("Student Not Found")

# -------------------------------------------------
# 3. Add a new student
# -------------------------------------------------
students["S131"] = {"name":"Rohan","marks":80}

print("\nNew Student Added")
print(students["S131"])

# -------------------------------------------------
# 4. Update marks of an existing student
# -------------------------------------------------
students["S101"]["marks"] = 90

print("\nUpdated Marks of S101")
print(students["S101"])

# -------------------------------------------------
# 5. Delete a student
# -------------------------------------------------
del students["S110"]

print("\nStudent S110 Deleted")

# -------------------------------------------------
# 6. Find Topper and Lowest Scorer
# -------------------------------------------------
topper = ""
lowest = ""

highest_marks = 0
lowest_marks = 100

for sid in students:

    marks = students[sid]["marks"]

    # Find highest marks
    if marks > highest_marks:
        highest_marks = marks
        topper = sid

    # Find lowest marks
    if marks < lowest_marks:
        lowest_marks = marks
        lowest = sid

print("\nTOPPER")
print(topper, students[topper])

print("\nLOWEST SCORER")
print(lowest, students[lowest])

# -------------------------------------------------
# 7. Calculate Class Average
# -------------------------------------------------
total = 0

for s in students.values():
    total = total + s["marks"]

average = total / len(students)

print("\nCLASS AVERAGE =", average)

# -------------------------------------------------
# 8. Count Pass and Fail Students
# Pass Marks = 50
# -------------------------------------------------
pass_count = 0
fail_count = 0

for s in students.values():

    if s["marks"] >= 50:
        pass_count += 1
    else:
        fail_count += 1

print("\nPASS STUDENTS =", pass_count)
print("FAIL STUDENTS =", fail_count)

# -------------------------------------------------
# 9. Generate Grades
# A = 90+
# B = 75-89
# C = 50-74
# F = Below 50
# -------------------------------------------------
print("\nSTUDENT GRADES")

for sid, s in students.items():

    marks = s["marks"]

    if marks >= 90:
        grade = "A"

    elif marks >= 75:
        grade = "B"

    elif marks >= 50:
        grade = "C"

    else:
        grade = "F"

    print(sid, s["name"], "-", grade)

# -------------------------------------------------
# 10. Display Students Scoring Above Average
# -------------------------------------------------
print("\nSTUDENTS ABOVE AVERAGE")

for sid, s in students.items():

    if s["marks"] > average:
        print(sid, s)

# -------------------------------------------------
# 11. Display Top 5 Performers
# No lambda used
# -------------------------------------------------
print("\nTOP 5 PERFORMERS")

# Create copy of dictionary
temp_students = students.copy()

for i in range(5):

    highest_id = ""
    highest_marks = -1

    # Find highest marks student
    for sid in temp_students:

        if temp_students[sid]["marks"] > highest_marks:

            highest_marks = temp_students[sid]["marks"]
            highest_id = sid

    print(highest_id, temp_students[highest_id])

    # Remove student after printing
    del temp_students[highest_id]

# -------------------------------------------------
# 12. Scholarship Students (Marks > 85)
# Create separate dictionary
# -------------------------------------------------
scholarship = {}

for sid, s in students.items():

    if s["marks"] > 85:
        scholarship[sid] = s

print("\nSCHOLARSHIP STUDENTS")

for sid, s in scholarship.items():
    print(sid, s)