'''
8. String-Based Attendance Tracker 
Problem Statement 
Attendance of a student for 15 days is represented as: 
PPAPPPAAPPPPAPP 
Where: 
• P = Present  
• A = Absent  
Tasks 
Write a program to: 
1. Count Present and Absent days.  
2. Calculate attendance percentage.  
3. Find the longest consecutive streak of Presence.  
4. Find the longest consecutive streak of Absence.  
5. Determine whether attendance is below 75%.  
Sample Output 
Attendance Record: 
PPAPPPAAPPPPAPP 
 
Present Days: 11 
Absent Days: 4 
 
Attendance Percentage: 73.33% 
 
Longest Present Streak: 4 
Longest Absent Streak: 2 
 
Attendance Status: Below 75% 
'''
# Attendance record for 15 days
attendance = "PPAPPPAAPPPPAPP"

# Count total Present days
present = attendance.count("P")

# Count total Absent days
absent = attendance.count("A")

# Find total number of days
total_days = len(attendance)

# Calculate attendance percentage
percentage = (present / total_days) * 100

# Variables to store longest and current Present streak
longest_p = 0
current_p = 0

# Find longest consecutive Present streak
for ch in attendance:

    # If student is Present
    if ch == "P":
        current_p += 1

        # Update longest streak if needed
        if current_p > longest_p:
            longest_p = current_p

    # If Absent, streak breaks
    else:
        current_p = 0

# Variables to store longest and current Absent streak
longest_a = 0
current_a = 0

# Find longest consecutive Absent streak
for ch in attendance:

    # If student is Absent
    if ch == "A":
        current_a += 1

        # Update longest streak if needed
        if current_a > longest_a:
            longest_a = current_a

    # If Present, streak breaks
    else:
        current_a = 0

# Check whether attendance is below 75%
if percentage < 75:
    status = "Below 75%"
else:
    status = "Above 75%"

# Display attendance record
print("Attendance Record:", attendance)

# Display Present and Absent counts
print("Present Days:", present)
print("Absent Days:", absent)

# Display attendance percentage
print("Attendance Percentage:", round(percentage, 2), "%")

# Display longest streaks
print("Longest Present Streak:", longest_p)
print("Longest Absent Streak:", longest_a)

# Display attendance status
print("Attendance Status:", status)
