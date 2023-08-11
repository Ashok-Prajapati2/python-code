"""
Prime Number Checker

This program checks if a given integer is a prime number.

Author: ASHOK KUMAR
Date: August 11, 2023
"""
print("Prime number checker")
def prime_check(n):
    is_prime = True
    for p in range(2,n):
        if n%p == 0:
            is_prime = False
    if is_prime:
        print(f"{n} is a prime number") 
    else:
        print(f"{n} is a not prime number")   
user_input = int(input("Enter number : "))         
prime_check(user_input)