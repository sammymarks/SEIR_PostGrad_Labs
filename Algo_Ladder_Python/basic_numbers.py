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

# print(primes(7))
# print(primes(math.floor(random.random()*1000)))
# print(primes(math.floor(random.random()*1000)))
# print(primes(math.floor(random.random()*1000)))

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

# fizzbuzz(30)

# Write a function that gives the Nth number of the Fibonacci Sequence. The Fibonacci sequence begins with 0 and 1, and every number thereafter is the sum of the previous two numbers. So the sequence goes like this:

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, and so on until infinity...

# Input: 9
# Output: 21 (as this is the 9th number of the Fibonacci Sequence)

def fibonacci(num):
    fib_list = [0,1]
    if num<2:
        return fib_list[num]
    else:
        i=2
        while i<num:
            fib_list.append(fib_list[i-1] + fib_list[i-2])
            i+=1
        return (fib_list[num-1])

# print(fibonacci(9))
# print(fibonacci(100))

# Given a year, report if it is a leap year.

# The tricky thing here is that a leap year in the Gregorian calendar occurs:

# on every year that is evenly divisible by 4
# except every year that is evenly divisible by 100
# unless the year is also evenly divisible by 400
# For example, 1997 is not a leap year, but 1996 is. 1900 is not a leap year, but 2000 is.

# If your language provides a method in the standard library that does this look-up, pretend it doesn't exist and implement it yourself.

def leap_year(year):
    if year%4 == 0:
        if year%100 == 0:
            if year%400 == 0:
                return f"{year}, True"
            return f"{year}, False"
        return f"{year}, True"
    else:
        return f"{year}, False"



# print(leap_year(1900))
# print(leap_year(1996))
# print(leap_year(1997))
# print(leap_year(2000))

# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

def three_five_sum(num):
    output = 0
    for n in range(num):
        if n%3==0 or n%5==0:
            output += n
    return output

# print(three_five_sum(10))
# print(three_five_sum(1000))


# The Collatz Conjecture or 3x+1 problem can be summarized as follows:

# Take any positive integer n. If n is even, divide n by 2 to get n / 2. If n is odd, multiply n by 3 and add 1 to get 3n + 1. Repeat the process indefinitely. The conjecture states that no matter which number you start with, you will always reach 1 eventually.

# Given a number n, return the number of steps required to reach 1.

# Examples
# Starting with n = 12, the steps would be as follows:

# 12
# 6
# 3
# 10
# 5
# 16
# 8
# 4
# 2
# 1

# Resulting in 9 steps. So for input n = 12, the return value would be 9.

def collatz(num):
    counter = 0

    while num != 1:
        counter += 1
        if num%2 == 0:
            num = num/2
        else:
            num = (num*3 +1)
    return counter

print(collatz(12))
print(collatz(5000))


from basic_string import palindrome

def largest_palindrome():
    
    largest = 0
    
    i=100
    while i<1000:
        j=100
        while j<1000:
            if palindrome(str(i*j)) == True:
                if i*j>largest:
                    largest = i*j
            j+=1
        i+=1
    return largest

print(largest_palindrome())