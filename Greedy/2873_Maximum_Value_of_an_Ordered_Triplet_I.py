from typing import List

# blackbox approach: TC O(n^3)
'''
class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        N = len(nums)
        for i in range(N):
            for j in range(i+1, N):
                for k in range(j+1, N):
                    res = max(res, (nums[i]-nums[j])*nums[k]) # blackbox approach
        return res
    '''


    # Greedy Approach: TC O(n^2)
    # max i, min j, max k

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res = 0
        N = len(nums)
        left = nums[0]
        for j in range(1,N):
            if nums[j] > left:
                left = nums[j]
            for k in range(j+1, N):
                res = max(res, (left-nums[j])*nums[k])
        return res
    
