#Problem Statement 
#An inventory manager stores stock quantities as: 
#stock = [25, 5, 0, 12, 3, 18, 0, 30] 
#Write a program to: 
#1. Display products that are out of stock.  
#2. Display products that need restocking (quantity less than 10).  
#3. Count available products.  
#4. Create a new list containing only products with stock greater than or equal to 15.  

print()
stock = [25, 5, 0, 12, 3, 18, 0, 30]

# 1. Out of stock count
out_of_stock = 0 # Initialize counter for out of stock products
for s in stock:# Loop through the stock list
    if s == 0:
        out_of_stock += 1 # Increment the counter if the product is out of stock
print("Out of Stock Products:", out_of_stock) 

# 2. Restock required (quantity < 10)
restock = []
for s in stock: 
    if s < 10: #check if the product needs restocking 
        restock.append(s) # Add the product to the restock list if it needs restocking
print("Restock Required:", restock)

# 3. Available products (quantity > 0)
available = 0 
for s in stock:
    if s > 0: 
        available += 1 # Increment the counter for available products if the quantity is greater than 0
print("Available Products:", available)# Print the count of available products

# 4. Healthy stock (quantity >= 15)
healthy = []
for s in stock:
    if s >= 15: # Check if the product has healthy stock
        healthy.append(s) # Add the product to the healthy stock list if it has healthy stock
print("Healthy Stock:", healthy)


