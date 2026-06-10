'''2. E-Commerce Inventory & Sales Dashboard 
Problem Statement 
An online store wants to manage products and sales. 
Example Structure 
products = { 
    "P101": { 
        "name": "Laptop", 
        "price": 55000, 
        "stock": 12, 
        "sold": 25 
    } 
} 
Maintain records of at least 30 products. 
Requirements 
1. Display all products.  
2. Add a new product.  
3. Update stock after sales.  
4. Find out-of-stock products.  
5. Find products with stock less than 5.  
6. Calculate total inventory value.  
7. Find best-selling product.  
8. Find least-selling product.  
9. Calculate total revenue generated.  
10. Generate a low-stock report.  
11. Display products whose sales exceed the average sales.  
12. Create a dictionary of products eligible for promotion (sales < 10).  
Challenge 
Generate a complete business report.
'''
# E-Commerce Inventory & Sales Dashboard

products = {
    "P101": {"name": "Laptop", "price": 55000, "stock": 12, "sold": 25},
    "P102": {"name": "Mouse", "price": 500, "stock": 3, "sold": 8},
    "P103": {"name": "Keyboard", "price": 1200, "stock": 0, "sold": 15},
    "P104": {"name": "Monitor", "price": 10000, "stock": 4, "sold": 5},
    "P105": {"name": "Printer", "price": 8000, "stock": 10, "sold": 20}
}

# 1. Display all products
print("All Products:")
for p in products:
    print(p, products[p])

# 2. Add a new product
products["P106"] = {"name": "Speaker", "price": 2000, "stock": 6, "sold": 7}

# 3. Update stock after sales
products["P101"]["stock"] -= 2
products["P101"]["sold"] += 2

# 4. Out of stock products
print("\nOut of Stock Products:")
for p in products:
    if products[p]["stock"] == 0:
        print(products[p]["name"])

# 5. Products with stock less than 5
print("\nStock Less Than 5:")
for p in products:
    if products[p]["stock"] < 5:
        print(products[p]["name"])

# 6. Total inventory value
inventory = 0
for p in products:
    inventory += products[p]["price"] * products[p]["stock"]
print("\nTotal Inventory Value =", inventory)

# 7. Best-selling product
best = ""
max_sale = 0
for p in products:
    if products[p]["sold"] > max_sale:
        max_sale = products[p]["sold"]
        best = products[p]["name"]
print("Best Selling Product =", best)

# 8. Least-selling product
least = ""
min_sale = 999999
for p in products:
    if products[p]["sold"] < min_sale:
        min_sale = products[p]["sold"]
        least = products[p]["name"]
print("Least Selling Product =", least)

# 9. Total revenue generated
revenue = 0
for p in products:
    revenue += products[p]["price"] * products[p]["sold"]
print("Total Revenue =", revenue)

# 10. Low-stock report
print("\nLow Stock Report:")
for p in products:
    if products[p]["stock"] < 5:
        print(products[p]["name"], "-", products[p]["stock"])

# 11. Products with sales above average
total_sales = 0
for p in products:
    total_sales += products[p]["sold"]

avg_sales = total_sales / len(products)

print("\nSales Above Average:")
for p in products:
    if products[p]["sold"] > avg_sales:
        print(products[p]["name"])

# 12. Promotion products (sales < 10)
promo = {}

for p in products:
    if products[p]["sold"] < 10:
        promo[p] = products[p]

print("\nPromotion Products:")
print(promo)

# Challenge: Business Report
print("\n----- BUSINESS REPORT -----")
print("Inventory Value =", inventory)
print("Revenue =", revenue)
print("Best Seller =", best)
print("Least Seller =", least)
print("Average Sales =", avg_sales)