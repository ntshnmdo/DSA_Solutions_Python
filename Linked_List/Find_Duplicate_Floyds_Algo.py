# LinkedList Cyclic prroblem
class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        
        # O(n) and O(n)

        seen = set()

        for i in nums:
            if i in seen:
                return i
            seen.add(i)

        # O(n) and O(1) constant space (Floyds Tortoise and Hare Algo)

        slow = 0
        fast = 0
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow2 = 0

        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                return slow

        