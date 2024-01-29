# Write a function that returns the reverse of a given string.

# Input: “abcde”
# Output: “edcba”

def reverse_string(string):
    print("reverse string")
    output = str()

    i = len(string)-1

    while i >= 0:
        output = output + string[i]
        i -= 1

    print (output)

reverse_string("abcde")

# Given a string, write a function that returns true if the “$” character is contained within the string or false if it is not.

# Input: “i hate $ but i love money i know i know im crazy”
# Output: true

# Input: “abcdefghijklmnopqrstuvwxyz”
# Output: false

def money(string):
    print("$ in String")
    output = False

    for char in string:
        if char == "$":
            output = True

    print (output)

money("i hate $ but i love money i know i know im crazy")
money("“abcdefghijklmnopqrstuvwxyz”")

# Given a string, write a function that returns a copy of the original string that has every other character capitalized. (Capitalization should begin with the second character.)

# Input: “hello, how are your porcupines today?”
# Output: “hElLo, HoW ArE YoUr pOrCuPiNeS ToDaY?”

def caps(string):
    print("Capitalize Every Other")
    output = str()

    counter = 0

    for char in string:
        if char.isalpha() == True:
            counter +=1
            if counter%2 == 0:
                output = output + char.capitalize()
            else:
                output = output + char
        else:
            output = output + char

    print(output)

caps("hello, how are your porcupines today?")


# Given a string, write a function that returns the first occurence of two duplicate characters in a row, and return the duplicated character.

# Input: “abcdefghhijkkloooop”
# Output: “h”

def duplicates(string):
    print("Duplicates")
    if len(string)<2:
        return "too short"
    else:
        i = 1
        while i<len(string):
            if string[i]==string[i-1]:
                return string[i]
            i+=1


print(duplicates("abcdefghhijkkloooop"))

def palindrome(string):
    print("Palindrome")
    check = True

    left = 0
    right = len(string)-1

    while right>left and check==True:
        if string[right]!=string[left]:
            check=False
        left += 1
        right -= 1

    return check
 
print(palindrome("racecar"))
print(palindrome("baloney"))

# Given two strings of equal length, write a function that returns the number of characters that are different between the two strings.

# Input: "ABCDEFG", "ABCXEOG"
# Output: 2

# Explanation: While the A, B, C, E, and G are in the same place for both strings, they have different characters in the other spaces. Since there are 2 such spaces that are different (the D and F in the first string), we return 2.

# Input: "ABCDEFG", "ABCDEFG",
# Output: 0

def hamming(str1, str2):
    output = 0
    i = 0
    while i<len(str1):
        if str1[i] != str2[i]:
            output += 1
        i+=1

    return output

print(hamming("ABCDEFG","ABCXEOG"))
print(hamming("ABCDEFG","ABCDEFG"))

# Given a string of words, write a function that returns a new string that contains the words in reverse order.

# Input: “popcorn is so cool isn’t it yeah i thought so”
# Output: “so thought i yeah it isn’t cool so is popcorn”

def split_reverse(string):
    split_list = string.split()
    reverse_list = []
    i = len(split_list) - 1

    while i>=0:
        reverse_list.append(split_list[i])
        i -= 1

    return " ".join(reverse_list)

print(split_reverse("popcorn is so cool isn’t it yeah i thought so"))