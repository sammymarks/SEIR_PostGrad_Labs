# Write a function that returns the sum of all numbers in a given array.

# NOTE: Do not use any built-in language functions that do this automatically for you.

# Input: [1, 2, 3, 4]
# Output: 10

# Explanation: (1 + 2 + 3 + 4) = 10



def basic_sum(arr):
    print("Basic Sum")
    output = 0

    for num in arr:
        output += num

    print(output)

basic_sum([1, 2, 3, 4])

# Given an array of numbers, write a function that returns a new array that contains all numbers from the original array that are less than 100.

# Input: [99, 101, 88, 4, 2000, 50]
# Output: [99, 88, 4, 50]



def less_than_100(arr):
    print("Less than 100")
    output = []
    for num in arr:
        if num < 100:
            output.append(num)
    print(output)



less_than_100([99, 101, 88, 4, 2000, 50])

# Given an array of numbers, write a function that returns a new array whose values are the original array’s value doubled.

# Input: [4, 2, 5, 99, -4]
# Output: [8, 4, 10, 198, -8]

def double(arr):
    print("Double")
    output = []
    for num in arr:
        output.append(num*2)
    print(output)

double([4, 2, 5, 99, -4])

# Write a function that returns the greatest value from an array of numbers.

# Input: [5, 17, -4, 20, 12]
# Output: 20

# (After you complete the exercise successfully, I recommend watching this video: Top US Coding Bootcamp | Actualize)

def greatest(arr):
    print("Greatest")
    greatest = int()
    for num in arr:
        if num>greatest:
            greatest = num
    print(greatest)

greatest([5, 17, -4, 20, 12])


# Write a function that accepts an array of numbers and returns the product of all the numbers.

# Input: [1, 2, 3, 4]
# Output: 24

# Explanation: (1 x 2 x 3 x 4) = 24

def product(arr):
    print("product")
    product = arr[0]
    if len(arr)==1:
        print(product)
    else:
        i=1
        while i<len(arr):
            product*=arr[i]
            i += 1
        print(product)

product([1, 2, 3, 4])
product([3])

# Given an array, write a function that returns an array that contains the original array’s values in reverse.

# Input: [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

def reverse(arr):
    print("reverse")
    rev = []
    
    i = len(arr)-1

    while i>=0:
        rev.append(arr[i])
        i -= 1
    print(rev)

reverse([1, 2, 3, 4, 5])

# Given an array of numbers, write a function that returns a new array in which only select numbers from the original array are included, based on the following details:

# The new array should always start with the first number from the original array. The next number that should be included depends on what the first number is. The first number dictates how many spaces to the right the computer should move to pick the next number. For example, if the first number is 2, then the next number that the computer should select would be two spaces to the right. This number gets added to the new array. If this next number happens to be a 4, then the next number after that is the one four spaces to the right. And so on and so forth until the end of the array is reached.

# Input:
# [2, 1, 3, 2, 5, 1, 2, 6, 2, 7, 1, 5, 6, 3, 2, 6, 2, 1, 2]

# Output:
# [2, 3, 1, 2, 2, 1, 5, 2, 2]

def skips(arr):
    print("skips")
    output = []
        
    i = 0

    while i<len(arr):
        output.append(arr[i])
        i += arr[i]
    print(output)

skips([2, 1, 3, 2, 5, 1, 2, 6, 2, 7, 1, 5, 6, 3, 2, 6, 2, 1, 2])