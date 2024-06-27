def maxSubArraysum(self, arr, size):
    sum = 0
    max_sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        max_sum = max(max_sum, sum)
        if sum<0:
            sum = 0
    
    return max_sum