import math 

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        
        
        # Brute FOrce Approach (TC: O(max(piles)*piles), SC: O(1))
        k = 1

        while True:
            totalTime = 0
            for p in piles:
                totalTime += math.ceil(p/k)
            
            if totalTime == h:
                return k
            k += 1
        return k
    
        # Binary Search Approach (TC: O(plogk), SC: O(1))

        l, r = 1, max(piles)
        res = r

        while l<=r:
            k = (l+r)//2
            hours = 0
            for p in piles:
                hours += math.ceil(p/k)
                if hours <= h:
                    res = min(res,k)
                    r = k-1
                else:
                    l = k+1
        return res