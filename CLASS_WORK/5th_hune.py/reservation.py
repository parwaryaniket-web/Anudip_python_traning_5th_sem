# 5. Bus Seat Reservation Analysis 
#Problem Statement 
#A bus has seats represented as: 
#seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0] 
#Where: 
#• 1 → Seat Booked  
#• 0 → Seat Available  
#Write a program to: 
#1. Count booked and available seats.  
#2. Find the first available seat and stop searching immediately.  
#3. Create a list of all available seat numbers.  
#4. Determine whether the bus is more than 70% occupied.  
print("---- BUS SEAT RESERVATION ANALYSES ----")
print()# Bus Seat Reservation Analysis
seats = [1, 0, 1, 1, 0, 0, 1, 1, 1, 0]# List representing bus seats
 
# 1. Count booked and available
booked = 0# Initialize counter for booked seats
available_count = 0
for s in seats:# Loop through the seats list
    if s == 1:# Check if the seat is booked
        booked += 1# Increment the booked counter if the seat is booked
    else:
        available_count += 1# Increment the available counter if the seat is available
print("Booked Seats:", booked)
print("Available Seats:", available_count)
 
# 2. First available seat (seat numbers start from 1)
for i in range(len(seats)):# Loop through the seats list
    if seats[i] == 0:# Check if the seat is available
        print("First Available Seat:", i + 1)# Print the first available seat number (index + 1)
        break
 
# 3. All available seat numbers
available_seats = []
for i in range(len(seats)):# Loop through the seats list
    if seats[i] == 0:# Check if the seat is available
        available_seats.append(i + 1)# Add the available seat number (index + 1) to the list of available seats
print("Available Seat Numbers:", available_seats)# Print the list of available seat numbers
 
# 4. Occupancy percentage
occupancy = (booked / len(seats)) * 100# Calculate the occupancy percentage based on the number of booked seats and total seats
print("Bus Occupancy:", str(int(occupancy)) + "%")
 
if occupancy > 70:# Check if the bus is more than 70% occupied
    print("Status: More Than 70% Occupied")#\
else:
    print("Status: Not More Than 70% Occupied")