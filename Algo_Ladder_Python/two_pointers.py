# Given two arrays of strings, return a new string that contains every combination of a string from the first array concatenated with a string from the second array.

# Input: ["a", "b", "c"], ["d", "e", "f", "g"]
# Output: ["ad", "ae", "af", "ag", "bd", "be", "bf", "bg", "cd", "ce", "cf", "cg"]

def array_mesh_one(one, two):
    output = []

    for i in one:
        for j in two:
            output.append(i+j)
    
    return output

print(array_mesh_one(["a", "b", "c"], ["d", "e", "f", "g"]))

# Given ONE array of strings, return a new array that contains every combination of each string with every other string in the array.

# Input: ["a", "b", "c", "d"]
# Output: ["ab", "ac", "ad", "ba", "bc", "bd", "ca", "cb", "cd", "da", "db", "dc"]

def array_mesh_two(arr):
    output = []
    i = 0
    while i<len(arr):
        j=0
        while j<len(arr):
            if i!=j:
                output.append(arr[i]+arr[j])
            j+=1
        i+=1
    return output

print(array_mesh_two(["a", "b", "c", "d"]))

# Find the largest product of any two numbers within a given array.

# Input: [5, -2, 1, -9, -7, 2, 6]
# Output: 63 (-9 * -7)

def largest_product(arr):
    output = arr[0]*arr[1]
    i = 0
    while i<len(arr):
        j=0
        while j<len(arr):
            if i!=j and arr[i]*arr[j]>output:
                    output = arr[i]*arr[j]
            j+=1
        i+=1
    return output

print(largest_product([5, -2, 1, -9, -7, 2, 6]))

# Given an array of numbers, return a new array containing just two numbers (from the original array) that add up to the number 10. If there are no two numbers that add up to 10, return false.

# Specifically use nested loops to solve this exercise even though there are other approaches as well.

# Input: [2, 5, 3, 1, 0, 7, 11]
# Output: [3, 7]

# Input: [1, 2, 3, 4, 5]
# Output: false (While 1, 2, 3, and 4 altogether add up to 10, we're seeking just one pair of numbers.)

# def two_sum_one(lst):
#     i = 0
#     while i<len(lst):
#         j=0
#         while j<len(lst):
#             if j!=i:
#                 if lst[i]+lst[j]==10:
#                     return [lst[i], lst[j]]
#             j+=1
#         i +=1
#     return False


def two_sum_one(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            if j!=i:
                if lst[i]+lst[j]==10:
                    return [lst[i], lst[j]]
    return False


print(two_sum_one([2, 5, 3, 1, 0, 7, 11]))
print(two_sum_one([1, 2, 3, 4, 5]))

# Given two sorted arrays, merge the second array into the first array while ensuring that the first array remains sorted. Do not use any built-in sort methods.

# Input :
# A : [1, 5, 8]
# B : [6, 9]

# Modified A : [1, 5, 6, 8, 9]

def merge_sort(lst1, lst2):

    output = []
    while len(lst1)*len(lst2)!=0:
        if lst1[0]<lst2[0]:
            output.append(lst1.pop(0))
        else:
            output.append(lst2.pop(0))
    # "*" is the spread operator in python
    output.append(*lst1, *lst2)
    return output

print(merge_sort([1, 5, 8], [6, 9]))

# Given an array of numbers, return true if the array is a "100 Coolio Array", or false if it is not.

# A "100 Coolio Array" meets the following criteria:

# Its first and last numbers add up to 100,
# Its second and second-to-last numbers add up to 100,
# Its third and third-to-last numbers add up to 100,
# and so on and so forth.

# Here are examples of 100 Coolio Arrays:

# [1, 2, 3, 97, 98, 99]
# [90, 20, 70, 100, 30, 80, 10]

def coolio(lst):
    i=0
    j=len(lst)-1
    check = True

    while i<=j and check==True:
        if i==j:
            if lst[i]!=100:
                check=False
        elif lst[i]+lst[j]!=100:
            check=False
        i+=1
        j-=1

    return check

print(coolio([1, 2, 3, 97, 98, 99]))
print(coolio([2, 2, 3, 97, 98, 99]))
print(coolio([90, 20, 70, 100, 30, 80, 10]))


# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.

    # SAMMY NOTES
    # setup a character counter (e.g., first character, second character)
    # setup a while loop that checks all words in the list at that character (against the first word as the placeholder)
    # If True, add the character to the output string
    # If False, break the loops and return the output string
    # False triggers when:
    #     characters of a word do not match
    #     there is no character in that word (e.g., word is too short)


def longest_prefix(lst):
    if len(lst)==0:
        return f"Prefix: "
    if len(lst) == 1:
        return f"Prefix: {lst[0]}"

    
    output = ""
    base_word = lst.pop(0)

    
    # loop through characters in base_word
    for i in range(len(base_word)):
        # loop through remaining words, first word was already removed
        for word in lst:
            # word is too short, break loop
            if len(word)<=i: 
                return f"Prefix: {output}"
            # word does not match, break loop
            elif word[i]!= base_word[i]:
                return f"Prefix: {output}"
        # No errors, add character to prefix output
        output += base_word[i]
    return f"Prefix: {output}"


print(longest_prefix(["flower","flow","flight"]))
print(longest_prefix(["flower"]))
print(longest_prefix(["flowe", "flowe"]))
print(longest_prefix(["flower","flow","flowers"]))
print(longest_prefix(["dog","racecar","car"]))