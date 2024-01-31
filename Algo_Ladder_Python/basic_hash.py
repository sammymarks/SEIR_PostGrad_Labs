import math

# Given a string, find the most commonly occurring letter.

# Input: “peter piper picked a peck of pickled peppers”
# Output: “p”

# SAMMY NOTES

# Create an object to store letters and counts
# Iterate over each letter in the input string
# For each letter, check the object (keys)
# If the key exists, increment the value by one
# If it doesn't exist, add a new key with letter and a value of 1

def frequent_letter(str):
    hash = {}

    # loop through string to document volume of characters
    for char in str:
        if char in hash.keys():
            hash[char]+=1
        else:
            hash[char] = 1
    
    highest = max(hash.values())

    # https://www.geeksforgeeks.org/python-get-key-from-value-in-dictionary/
    highest_index = (list(hash.values())).index(highest)
    return list(hash.keys())[highest_index]

print(frequent_letter("peter piper picked a peck of pickled peppers"))


# Given an array of strings, return a hash that provides of a count of how many times each string occurs.

# Input: ["Dewey", "Truman", "Dewey", "Dewey", "Truman", "Truman", "Dewey", "Truman", "Truman", "Dewey", "Dewey"]

# Output: {"Dewey" => 6, "Truman" => 5}

# Explanation: "Dewey" occurs 6 times in the array, while "Truman" occurs 5 times.

def count_votes(lst):
    hash = {}

    for str in lst:
        if str in hash.keys():
            hash[str]+=1
        else:
            hash[str]=1

    return hash


print(count_votes(["Dewey", "Truman", "Dewey", "Dewey", "Truman", "Truman", "Dewey", "Truman", "Truman", "Dewey", "Dewey"]))

# Given a hash, where the keys are strings representing food items, and the values are numbers representing the price of each food, return the amount someone would pay if they'd order one of each food from the entire menu.

# Input: {"hot dog" => 2, "hamburger" => 3, "steak sandwich" => 5, "fries" => 1, "cole slaw" => 1, "soda" => 2}

# Output: 14

# Explanation: If someone would order one of everything on the menu, they'd pay a total of 14 (the sum of all the hash's values).

def whole_menu(hash):
    return sum(hash.values())

print(whole_menu({"hot dog" : 2, "hamburger" : 3, "steak sandwich" : 5, "fries" : 1, "cole slaw" : 1, "soda" : 2}))

# Given an array of hashes that represent a list of social media posts, return a new array that only contains the posts that have at least 1000 likes.

# Input: [
# {title: 'Me Eating Pizza', submitted_by: "Joelle P.", likes: 1549},
# {title: 'i never knew how cool i was until now', submitted_by: "Lyndon Johnson", likes: 3},
# {title: 'best selfie evar!!!', submitted_by: "Patti Q.", likes: 1092},
# {title: 'Mondays are the worst', submitted_by: "Aunty Em", likes: 644}
# ]

# Output: [
# {title: 'Me Eating Pizza', submitted_by: "Joelle P.", likes: 1549},
# {title: 'best selfie evar!!!', submitted_by: "Patti Q.", likes: 1092},
# ]

def popular_posts(hash_list):
    output = []
    for h in hash_list:
        if h["likes"]>=1000:
            output.append(h)
    return output

print(popular_posts([
{"title": 'Me Eating Pizza', "submitted_by": "Joelle P.", "likes": 1549},
{"title": 'i never knew how cool i was until now', "submitted_by": "Lyndon Johnson", "likes": 3},
{"title": 'best selfie evar!!!', "submitted_by": "Patti Q.", "likes": 1092},
{"title": 'Mondays are the worst', "submitted_by": "Aunty Em", "likes": 644}
]))

# Given a DNA strand, return its RNA complement (per RNA transcription).

# Both DNA and RNA strands are a sequence of nucleotides. Here we're representing the sequences with single-letter characters (e.g. a sample strand may look like: "AGCA".)

# Given a string representing a DNA strand, provide its transcribed RNA strand, according to the following pattern:

# G becomes C
# C becomes G
# T becomes A
# A becomes U

# So based on all this, here's a sample input/output:

# Input: 'ACGTGGTCTTAA'
# Output: 'UGCACCAGAAUU'



def RNA(input):
    output = ""

    rules = {
        "G":"C",
        "C":"G",
        "T":"A",
        "A":"U"
    }

    for char in input:
        output += rules[char]

    return output

print(RNA("ACGTGGTCTTAA"))

# Given an array of social media posts and a hash of users, return a list of posts (as an array of hashes) that replaces the submitted_by id number as the person's actual name.

# For example, given this array of posts (note that the submitted_by is an id number):

# [
# {title: 'Me Eating Pizza', submitted_by: 231, likes: 1549},
# {title: 'i never knew how cool i was until now', submitted_by: 989, likes: 3},
# {title: 'best selfie evar!!!', submitted_by: 111, likes: 1092},
# {title: 'Mondays are the worst', submitted_by: 403, likes: 644}
# ]

# And this hash of users (the key is the id number and the value is the user's real name):

# users = {403 => "Aunty Em", 231 => "Joelle P.", 989 => "Lyndon Johnson", 111 => "Patti Q."}

# Return the array of posts as follows:

# [
# {title: 'Me Eating Pizza', submitted_by: "Joelle P.", likes: 1549},
# {title: 'i never knew how cool i was until now', submitted_by: "Lyndon Johnson", likes: 3},
# {title: 'best selfie evar!!!', submitted_by: "Patti Q.", likes: 1092},
# {title: 'Mondays are the worst', submitted_by: "Aunty Em", likes: 644}
# ]

def complete_data(posts, users):
    for dict in posts:
        username = users[dict["submitted_by"]]
        dict["submitted_by"]=username
    return posts



posts = [
{"title": 'Me Eating Pizza', "submitted_by": 231, "likes": 1549},
{"title": 'i never knew how cool i was until now', "submitted_by": 989, "likes": 3},
{"title": 'best selfie evar!!!', "submitted_by": 111, "likes": 1092},
{"title": 'Mondays are the worst', "submitted_by": 403, "likes": 644}
]

users = {403 : "Aunty Em", 231 : "Joelle P.", 989 : "Lyndon Johnson", 111 : "Patti Q."}

print(complete_data(posts, users))


# Given two strings, return true if they are anagrams of each other, and false if they are not. An anagram is a word, phrase, or name formed by rearranging the letters of another, such as cinema, formed from iceman.

# Do not use any built-in sort methods.

# Input: “silent”, “listen”
# Output: true

# Input: “frog”, “bear”
# Output: false

def anagrams(one, two):
    
    #check if the words are the same length
    if len(one)!=len(two):
        return False

    hash_one = {}
    hash_two = {}

    # Define first hash
    for char in one:
        if char in hash_one.keys():
            hash_one[char]+=1
        else:
            hash_one[char] = 1

    #define second hash
    for char in two:
        if char in hash_two.keys():
            hash_two[char]+=1
        else:
            hash_two[char] = 1

    # For each key in first hash
    for k in list(hash_one.keys()):
        # check if the key does not exist in the second hash
        if k not in hash_two.keys():
            return False
        # or if the frequency of letters is different
        elif hash_one[k]!=hash_two[k]:
            return False
    
    return True

print(anagrams("silent", "listen"))
print(anagrams("silent", "listenz"))
print(anagrams("frog", "bear"))