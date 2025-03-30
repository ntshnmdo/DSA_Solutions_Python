class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        
        # TC: O(nlogn) and SC: O(n)
        nums.sort()
        res = []

        for i in range (0, len(nums)-1):
            if nums[i] == nums[i+1]:
                res.append(nums[i])
                i += 1
            else:
                i += 1
        return res