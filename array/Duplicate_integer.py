# Brute Force: TC_O(n.n) and SC_O(1)

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False   
    
# Sorting: TC_O(n) SC_O(1)

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i -1]:
                return True
        return False
    
# Hash Set TC_O(n) and SC_O(n)

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
    
# Hash_set_length: TC_O(n) and SC_O(n)

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums)) < len(nums)