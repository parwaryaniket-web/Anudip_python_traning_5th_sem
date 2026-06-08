'''1. Online Shopping Order Analytics 
Problem Statement 
An e-commerce company stores product sales data as: 
sales = { 
    "Laptop": 15, 
    "Mouse": 45, 
    "Keyboard": 32, 
    "Monitor": 12, 
    "Headphones": 28, 
    "Printer": 8, 
    "Webcam": 20, 
    "Speaker": 18, 
    "Tablet": 10, 
    "Router": 25 
} 
Tasks 
1. Display products sold more than 20 times.  
2. Find the best-selling product.  
3. Find the least-selling product.  
4. Calculate total products sold.  
5. Create a list of products requiring promotion (sales < 15).  
6. Count products having sales between 10 and 30.  
Sample Output 
Products Sold More Than 20 Times: 
Mouse 
Keyboard 
Headphones 
Router 
 
Best Selling Product: Mouse (45) 
 
Least Selling Product: Printer (8) 
 
Total Units Sold: 213 
 
Products Requiring Promotion: 
['Monitor', 'Printer', 'Tablet'] 
 
Products Having Sales Between 10 and 30: 6
'''
# Online Shopping Order Analytics

sales = {
    "Laptop": 15,
    "Mouse": 45,
    "Keyboard": 32,
    "Monitor": 12,
    "Headphones": 28,
    "Printer": 8,
    "Webcam": 20,
    "Speaker": 18,
    "Tablet": 10,
    "Router": 25
}

# 1. Products sold more than 20 times
print("Products Sold More Than 20 Times:")

# for loop picks one product at a time from the dictionary
for product in sales:

    # check if the sales of the current product are greater than 20
    if sales[product] > 20:

        # print the product if the condition is True
        print(product)

# 2. Find the best-selling product

# stores the name of the best-selling product
best_product = ""

# stores the highest sales found so far
best_sales = 0

# check every product in the dictionary
for product in sales:

    # compare current product sales with highest sales found so far
    if sales[product] > best_sales:

        # update highest sales
        best_sales = sales[product]

        # update best-selling product name
        best_product = product

print("\nBest Selling Product:", best_product, "(", best_sales, ")")


# 3. Find the least-selling product

# stores the name of the least-selling product
least_product = ""

# stores the lowest sales found so far
least_sales = 1000

# check every product
for product in sales:

    # compare current product sales with lowest sales found so far
    if sales[product] < least_sales:

        # update lowest sales
        least_sales = sales[product]

        # update least-selling product
        least_product = product

print("\nLeast Selling Product:", least_product, "(", least_sales, ")")


# 4. Calculate total products sold

# variable to store total sales
total = 0

# go through every product
for product in sales:

    # add current product sales to total
    total = total + sales[product]

print("\nTotal Units Sold:", total)


# 5. Products requiring promotion

# empty list to store products with sales less than 15
promotion = []

# check every product
for product in sales:

    # if sales are less than 15
    if sales[product] < 15:

        # add product name to the promotion list
        promotion.append(product)

print("\nProducts Requiring Promotion:")
print(promotion)


# 6. Count products having sales between 10 and 30

# variable to count products
count = 0

# check every product
for product in sales:

    # check if sales are between 10 and 30
    if sales[product] >= 10 and sales[product] <= 30:

        # increase count by 1
        count += 1

print("\nProducts Having Sales Between 10 and 30:", count)