# Prime Number Analyzer
# This program checks if a given number is prime and lists all prime numbers up to that number.
#If the number is not prime, display all its factors. 
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def prime_factors(num):
    factors = []
    for i in range(2, num + 1):
        while num % i == 0:
            factors.append(i)
            num //= i
    return factors  
number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
    print(f"The prime factors of {number} are: {prime_factors(number)}")