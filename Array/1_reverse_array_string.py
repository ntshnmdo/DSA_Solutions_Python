def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
# TC:O(n), SC:O(1)
A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is ")
print(A)

#1 Using  Slicing  TC: O(n), SC: O(n) because a new list is created

def reverse_array(arr):
    return arr[::-1]

#2 Using Two-Pointer Approach (efficient, in-phase), TC: O(n), SC:O(1) modifies original list

def reverse_array(arr):
    left, right = 0, len(arr)-1
    while left<right:
        arr[left], arr[right] = arr[right], arr[left] # swap element
        left += 1
        right -= 1

reverse_array(arr) 

#3 Using Python built in reverse() method (modifies in place), TC: O(n) SC: O(1)

arr.reverse()
