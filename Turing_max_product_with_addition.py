# Let's say there is one array [2, 4, 3] and positive integer 5, we have to add numbers that sum to 5 to elements of 
# given array [2, 4, 3] in such a way that the product of all the elements is maximum.

# Example: given array = [2,4,3] 
#                Positive Integer = 5
#                result array = [5, 4, 5]
#                Product = 100

import heapq

def max_product_with_additions(nums, k):
    # create a min-heap from the original array
    min_heap = nums[:]
    heapq.heapify(min_heap)

    # distribute 'k' across the elements in the heap
    while k>0:
        # extract the smallest element from the heap
        smallest = heapq.heappop(min_heap)
        # increment the smallest element
        smallest += 1
        # push the incremented element back into the heap
        heapq.heappush(min_heap, smallest)
        # decrement k
        k -= 1

    # calculate the final product of the elements in the heap
    product = 1 
    for num in min_heap:
        product *= num

    return product

# example 
nums = [4, 2, 1, 3, 6]
k = 15
output = max_product_with_additions(nums, k)
print(output)  