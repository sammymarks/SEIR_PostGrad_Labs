# Given two arrays, return a new array that contains the intersection of the two arrays. The intersection means the values that are contained in both of the arrays. Do not use the "&", or any built-in intersection methods.

# NOTE: You must accomplish this in O(n) time. This is also known as linear time.

# Input: [1, 2, 3, 4, 5], [1, 3, 5, 7, 9]
# Output: [1, 3, 5]

def array_intersection(one, two):
    output = []
    hash_one = {}
    for o in one:
        hash_one[o] = True

    for t in two:
        if t in hash_one.keys():
            output.append(t)
    return output


# O(N + N + 1) => O(2N + 1 ) => O(N) is linear complexity
print(array_intersection([1, 2, 3, 4, 5], [1, 3, 5, 7, 9]))

# Given two arrays, determine whether one is a subset of the other. It is considered a subset if all the values in one array are contained within the other.

# NOTE: You must accomplish this in O(n) time. This is also known as linear time.

# Input: [1, 2, 3, 4, 5, 6], [6, 3, 2]
# Output: true

# Input: [1, 2, 3, 4, 5, 6], [6, 3, 7]
# Output: false


def compare_subset(longer, shorter):
    hash_longer = {}
    #O(N)
    for el in longer:
        hash_longer[el] = True
    
    #O(N)
    for el in shorter:
        # O(1)
        if el not in hash_longer.keys():
            return False
    return True
    

def subset(one, two):
    # O(1)
    if len(one) >= len(two):
        return compare_subset(one, two)
    else:
        return compare_subset(two, one)

# Complexity = O(2N +2) => Linear

print(subset([1, 2, 3, 4, 5, 6], [6, 3, 2]))
print(subset([1, 2, 3, 4, 5, 6], [6, 3, 7]))

# A given array has one pair of duplicate values. Return the first duplicate value.

# NOTE: You must accomplish this in O(n) time. This is also known as linear time.

# Input: [5, 2, 9, 7, 2, 6]
# Output: 2

def duplicate(input):
    hash = {}
    for el in input:
        if el in hash.keys():
            return el
        else:
            hash[el]=True
    
    return "No Duplicates"

print(duplicate([5, 2, 9, 7, 2, 6]))

# A given string contains all the letters from the alphabet except for one. Return the missing letter.

# NOTE: You must accomplish this in O(n) time. This is also known as linear time.

# Input: “The quick brown box jumps over a lazy dog”
# Output: “f”

def missing_letter(input):
    lowercase = input.lower()

    alphabet_hash = {
        "a":0,
        "b":0,
        "c":0,
        "d":0,
        "e":0,
        "f":0,
        "g":0,
        "h":0,
        "i":0,
        "j":0,
        "k":0,
        "l":0,
        "m":0,
        "n":0,
        "o":0,
        "p":0,
        "q":0,
        "r":0,
        "s":0,
        "t":0,
        "u":0,
        "v":0,
        "w":0,
        "x":0,
        "y":0,
        "z":0,
    }

    for char in lowercase:
        if char.isalpha():
            alphabet_hash[char]+=1

    result = [i for i in alphabet_hash if alphabet_hash[i]==0]
    return result[0]
    
    
print(missing_letter("The quick brown box jumps over a lazy dog"))


# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

# NOTE: You must accomplish this in O(n) time. This is also known as linear time.

# Examples:

# s = "leetcode"
# return 0.
# (The "l" is the first character that only appears once in the string, and appears at index 0.)

# s = "loveleetcode",
# return 2.
# (The "l" and "o" are repeated, so the first non-repeating character is the "v", which is at index 2.)

# Note: You may assume the string contain only lowercase letters.

# Loop through the strings once -> O(N)
# Create a hashtable with the following format:
# {"letter" : {
#     "count" : num,
#     "index" : num
# }}
# Loop throught he hashtable once -> O(N) to return the index first letter where count  = 1

# O(2N) -> Linesar

def appears_once(str):
    hash = {}

    for i in range(len(str)):
        char=str[i]
        if char in hash.keys():
            hash[char]["count"] += 1
        else:
            hash[char] = {
                "count" : 1,
                "index" : i
                }
    
    for key in hash.keys():
        if hash[key]["count"]==1:
            return hash[key]["index"]

print(appears_once("leetcode"))
print(appears_once("loveleetcode"))


# This is the same exercise as Two Sum I, but you must now solve it in linear time.

# Given an array of numbers, return a new array containing just two numbers (from the original array) that add up to the number 10. If there are no two numbers that add up to 10, return false.

# Input: [2, 5, 3, 1, 0, 7, 11]
# Output: [3, 7]

# Input: [1, 2, 3, 4, 5]
# Output: false (While 1, 2, 3, and 4 altogether add up to 10, we're seeking just one pair of numbers.)

# Notes
# set hash
# loop through list
# if target - num is in hash, return the pair
# else add num to hash


def two_sum_linear(input, target):
    hash = {}

    # Linear O(N)
    for num in input:
        # Hash/Dict lookup is "Free" - O(1)
        if target-num in hash.keys():
            return [num, target-num]
        else:
            hash[num] = True

    return False

print(two_sum_linear([2, 5, 3, 1, 0, 7, 11], 10))
print(two_sum_linear([1, 2, 3, 4, 5], 10))

# This is very similar to ETL #3, but you must now accomplish the task in linear time (O(N)).

# Given an array of Youtube videos, for example:

# [
# {title: 'How to Make Wood', author_id: 4, views: 6},
# {title: 'How to Seem Perfect', author_id: 4, views: 111},
# {title: 'Review of the New "Unbreakable Mug"', author_id: 2, views: 202},
# {title: 'Why Pigs Stink', author_id: 1, views: 12}
# ]

# and an array of authors, for example:

# [
# {id: 1, first_name: 'Jazz', last_name: 'Callahan'},
# {id: 2, first_name: 'Ichabod', last_name: 'Loadbearer'},
# {id: 3, first_name: 'Saron', last_name: 'Kim'},
# {id: 4, first_name: 'Teena', last_name: 'Burgess'},
# ]

# Return a new array of videos in the following format, and only include videos that have at least 100 views:

# [
# {title: 'How to Seem Perfect', views: 111, author_name: 'Teena Burgess' }
# {title: 'Review of the New "Unbreakable Mug"', views: 202, author_name: 'Ichabod Loadbearer' },
# ]

# See ELT_Three in Data Transformations.