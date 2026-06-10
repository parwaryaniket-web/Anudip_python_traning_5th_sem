'''
2. Food Delivery Performance Tracker 
Problem Statement 
Delivery times (in minutes) for different orders are given below: 
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18] 
Requirements 
Create the following functions: 
1. fastest_delivery(times) 
Returns the shortest delivery time. 
2. delayed_orders(times) 
Returns a list of orders taking more than 45 minutes. 
3. average_delivery_time(times) 
Returns the average delivery time. 
4. delivery_category(times) 
Displays order categories: 
• Fast → ≤ 30 minutes  
• Normal → 31–45 minutes  
• Delayed → > 45 minutes  
Sample Output 
Fastest Delivery: 18 minutes 
 
Delayed Orders: 
[60, 80, 55] 
 
Average Delivery Time: 
40.8 minutes 
 
Categories: 
28 -> Fast 
45 -> Normal 
60 -> Delayed
'''
# =====================================
# Food Delivery Performance Tracker
# =====================================

# List storing delivery times (in minutes)
delivery_time = [28, 45, 60, 22, 35, 80, 40, 25, 55, 18]

# -------------------------------------
# Function to find fastest delivery
# -------------------------------------
def fastest_delivery(times):

    # Return minimum time
    return min(times)


# -------------------------------------
# Function to find delayed orders
# -------------------------------------
def delayed_orders(times):

    # Empty list to store delayed orders
    delayed = []

    # Check each delivery time
    for time in times:

        # More than 45 minutes = Delayed
        if time > 45:
            delayed.append(time)

    return delayed


# -------------------------------------
# Function to calculate average time
# -------------------------------------
def average_delivery_time(times):

    # Total of all delivery times
    total = sum(times)

    # Number of orders
    count = len(times)

    # Average formula
    average = total / count

    return average


# -------------------------------------
# Function to display categories
# -------------------------------------
def delivery_category(times):

    print("Categories:")

    # Check each delivery time
    for time in times:

        # Fast delivery
        if time <= 30:
            print(time, "-> Fast")

        # Normal delivery
        elif time <= 45:
            print(time, "-> Normal")

        # Delayed delivery
        else:
            print(time, "-> Delayed")


# =====================================
# Main Program
# =====================================

# Fastest delivery
print("Fastest Delivery:", fastest_delivery(delivery_time), "minutes")

# Delayed orders
print("\nDelayed Orders:")
print(delayed_orders(delivery_time))

# Average delivery time
print("\nAverage Delivery Time:")
print(round(average_delivery_time(delivery_time), 1), "minutes")

print()

# Display categories
delivery_category(delivery_time)