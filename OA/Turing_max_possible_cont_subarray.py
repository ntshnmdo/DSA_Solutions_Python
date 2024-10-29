from math import gcd
from typing import List

def max_contiguous_subarrays(arr: List[int]) -> List[List[int]]:
    n = len(arr)
    result = []

    # Iterating through the array for the  start index
    for start in range(n):
        for end in range(start+1, n):
            # check if first and last element of sub array have a GCD greater  than 1
            if gcd(arr[start], arr[end]) > 1:
                result.append(arr[start:end+1]) # store the subarray if valid 
                break # break to aviod unnecessary extensions of the subarray

    return result if result else 0

# test the function with the given example
arr = [6, 1, 2, 3, 4, 3]
print(max_contiguous_subarrays(arr))