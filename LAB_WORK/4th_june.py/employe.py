#10. Mini Employee Payroll System 
#Accept
#• Employee Name  
#• Basic Salary  
#HRA 20% 
#DA 10% 
#PF Deduction 12% 
#Calculate and display
#• Gross Salary
#• Net Salary   
print("-----MINI EMPLOYEE PAYROLL SYSTEM-----")
employee_name = input("Enter employee name: ")  
basic_salary = float(input("Enter basic salary: "))
hra = 0.20 * basic_salary
da = 0.10 * basic_salary
pf_deduction = 0.12 * basic_salary
gross_salary = basic_salary + hra + da
net_salary = gross_salary - pf_deduction
print(f"Employee Name: {employee_name}")
print(f"Gross Salary: ₹{gross_salary:.2f}") 
print(f"Net Salary: ₹{net_salary:.2f}")