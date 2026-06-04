#5. Electricity Bill Calculator 
#Calculate electricity bill based on the following slab rates: 
#Units Rate 
#0-100 ₹5/unit 
#101-200 ₹7/unit 
#Above 200 ₹10/unit 
print("-----ELECTRICITY BILL CALCULATOR-----")  
units = int(input("Enter the number of units consumed: "))
if units <= 100:
    bill_amount = units * 5
elif units <= 200:
    bill_amount = 100 * 5 + (units - 100) * 7
else:
    bill_amount = 100 * 5 + 100 * 7 + (units - 200) * 10

print(f"Electricity Bill: ₹{bill_amount}")
