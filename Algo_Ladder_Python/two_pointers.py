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