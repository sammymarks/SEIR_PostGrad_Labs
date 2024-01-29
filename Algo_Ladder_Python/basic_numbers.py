# Write a function that returns whether a given number is a prime number.

import random
import math

def primes(num):
    check = True

    if num <2:
        return "invalid entry"
    elif num == 2:
        return f"{num} is Prime"
    else:
        check=True
        i=2
        while i<num and check==True:
            if num%i == 0:
                check=False
            i+=1
        
        if check==True:
            return f"{num} is Prime"
        else:
            return f"{num} is not Prime"

print(primes(7))
print(primes(math.floor(random.random()*1000)))
print(primes(math.floor(random.random()*1000)))
print(primes(math.floor(random.random()*1000)))

# Write a function that prints out every number from 1 to N, with the following exceptions:

# If the number is divisible by 3, print out "FIZZ".
# If the number is divisible by 5, print out "BUZZ".
# If the number is divisible by both 3 and 5, print out "FIZZBUZZ".

def fizzbuzz(num):
    for a in range(num):
        n = a+1
        if n%3==0 and n%5==0:
            print("FIZZBUZZ")
        elif n%3==0:
            print("FIZZ")
        elif n%5==0:
            print("BUZZ")
        else:
            print(n)

fizzbuzz(30)