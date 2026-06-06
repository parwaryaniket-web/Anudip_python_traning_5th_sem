# Flight Booking Analysis
# Problem Statement
#A flight reservation system stores passenger records as tuples: 
#bookings = ( 
#    ("P101", "Delhi", "Confirmed"), 
#    ("P102", "Mumbai", "Waiting"), 
#   ("P103", "Delhi", "Confirmed"), 
#    ("P104", "Chennai", "Cancelled"), 
#    ("P105", "Mumbai", "Confirmed"), 
#    ("P106", "Delhi", "Waiting") 
#) 
#Where: 
#• Passenger ID  
#• Destination  
#• Booking Status  
#Tasks 
#Write a Python program to: 
#1. Display all passengers whose booking status is Confirmed.  
#2. Count the number of passengers travelling to Delhi.  
#3. Count Confirmed, Waiting, and Cancelled bookings separately.  
#4. Create a list containing passenger IDs with Waiting status.  
#5. Determine which destination has the highest number of bookings. 
print("---- FLIGHT BOOKING ANALYSIS ----")
# Store all booking records in a tuple
bookings = (
    ("P101", "Delhi", "Confirmed"),
    ("P102", "Mumbai", "Waiting"),
    ("P103", "Delhi", "Confirmed"),
    ("P104", "Chennai", "Cancelled"),
    ("P105", "Mumbai", "Confirmed"),
    ("P106", "Delhi", "Waiting")
)

# Print heading for confirmed passengers
print("Confirmed Passengers:")

# Loop through each booking record
for pid, city, status in bookings:
    
    # Check if booking status is Confirmed
    if status == "Confirmed":
        
        # Print passenger ID and destination
        print(pid, city)

# Count passengers travelling to Delhi and print the result
print("\nPassengers Travelling to Delhi:",
      sum(1 for _, city, _ in bookings if city == "Delhi"))

# Count all Confirmed bookings
print("\nConfirmed:",
      sum(1 for _, _, s in bookings if s == "Confirmed"))

# Count all Waiting bookings
print("Waiting:",
      sum(1 for _, _, s in bookings if s == "Waiting"))

# Count all Cancelled bookings
print("Cancelled:",
      sum(1 for _, _, s in bookings if s == "Cancelled"))

# Create a list containing IDs of passengers with Waiting status
waiting = [pid for pid, _, s in bookings if s == "Waiting"]

# Display the waiting list
print("\nWaiting List:", waiting)

# Create a list of all destinations
cities = [city for _, city, _ in bookings]

# Find the destination that appears the most times
most_booked = max(set(cities), key=cities.count)

# Display the most booked destination
print("\nMost Booked Destination:", most_booked)


