'''
1. Railway Reservation Seat Analyzer 
Problem Statement 
A railway coach has seats represented as follows: 
seats = [ 
    "Booked", "Available", "Booked", "Booked", 
    "Available", "Available", "Booked", "Available", 
    "Booked", "Booked", "Available", "Booked" 
] 
Requirements 
Create the following functions: 
1. count_seats(seats) 
Returns the number of booked and available seats. 
2. first_available(seats) 
Returns the seat number of the first available seat. 
3. occupancy_percentage(seats) 
Returns the percentage of occupied seats. 
4. display_available_seats(seats) 
Displays all available seat numbers. 
Sample Output 
Booked Seats: 7 
Available Seats: 5 
 
First Available Seat: 2 
 
Occupancy Percentage: 58.33% 
 
Available Seat Numbers: 
2 5 6 8 11
'''
# =====================================
# Railway Reservation Seat Analyzer
# =====================================

# List storing seat status
seats = [
    "Booked", "Available", "Booked", "Booked",
    "Available", "Available", "Booked", "Available",
    "Booked", "Booked", "Available", "Booked"
]

# -------------------------------------------------
# Function to count booked and available seats
# -------------------------------------------------
def count_seats(seats):

    # Count booked seats
    booked = seats.count("Booked")

    # Count available seats
    available = seats.count("Available")

    # Return both values
    return booked, available


# -------------------------------------------------
# Function to find first available seat
# -------------------------------------------------
def first_available(seats):

    # Loop through all seats
    for i in range(len(seats)):

        # Check if seat is available
        if seats[i] == "Available":

            # +1 because seat numbering starts from 1
            return i + 1

    # If no seat is available
    return "No Seat Available"


# -------------------------------------------------
# Function to calculate occupancy percentage
# -------------------------------------------------
def occupancy_percentage(seats):

    # Count booked seats
    booked = seats.count("Booked")

    # Total number of seats
    total = len(seats)

    # Calculate percentage
    percentage = (booked / total) * 100

    return percentage


# -------------------------------------------------
# Function to display available seat numbers
# -------------------------------------------------
def display_available_seats(seats):

    print("Available Seat Numbers:")

    # Loop through all seats
    for i in range(len(seats)):

        # Check available seats
        if seats[i] == "Available":

            # Print seat number
            print(i + 1, end=" ")

    print()


# =====================================
# Main Program
# =====================================

# Call count function
booked, available = count_seats(seats)

print("Booked Seats:", booked)
print("Available Seats:", available)

# Call first available function
print("\nFirst Available Seat:", first_available(seats))

# Call occupancy percentage function
print("\nOccupancy Percentage:", round(occupancy_percentage(seats), 2), "%")

print()

# Call display function
display_available_seats(seats)
