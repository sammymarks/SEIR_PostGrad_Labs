import math

# Binary Search Algorithm – Iterative and Recursive Implementation
# Given a sorted array of n integers and a target value, determine if the target exists in the array in logarithmic time using the binary search algorithm. If target exists in the array, print the index of it.

# start with def initiate_binary_search(sorted_list, target)

# inside initiate_binary_search -> create binary_search(left_index, right_index, middle_index, target)
#     if len(list) = 0:
#         return False
#     elif list[middle_index] == target:
#         return middle_index
#     elif list[middle] < target:
#         return binary_search(left = 0, right = middle, middle = middle-left/2)
#     else -> if list[middle] > target: 

def initiate_binary_search(sorted, target):
    initial_left = 0
    initial_right = len(sorted)-1

    def binary_search(left, right):
        print([left, right])
        #single case
        if left==right:
            if sorted[left]==target:
                return left
            else:
                return False

        #double case
        elif right-left == 1:
            if sorted[left]==target:
                return left
            elif sorted[right]==target:
                return right
            else:
                return False

        #recursion case
        else:

            middle = math.floor((right-left)/2) + left        
            # check if final box
            if sorted[middle]==target:
                return middle
            elif sorted[middle]>target:
                return binary_search(left, middle)
            else:
                return binary_search(middle, right)
            


    return binary_search(initial_left, initial_right)

print(initiate_binary_search([2, 3, 5, 7, 9], 7))
print(initiate_binary_search([1, 3, 4, 5, 8, 9], 2))
print(initiate_binary_search([1, 2, 4, 5, 8, 9], 2))