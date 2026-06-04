#3. Strong Number Verification 
#A Strong Number is a number whose sum of factorials of digits equals the number itself. 
#Write a program to check whether a given number is a Strong Number. 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
def is_strong_number(num):
    sum_of_factorials = sum(factorial(int(digit)) for digit in str(num))
    return sum_of_factorials == num

number = int(input("Enter a number: "))
if is_strong_number(number):
    print(f"{number} is a Strong Number.")
else:
    print(f"{number} is not a Strong Number.")  