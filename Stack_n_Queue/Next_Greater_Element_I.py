class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # TC: O(m+n), SC: O(m)
        
        nums1Idx = { n:i for i, n in enumerate(nums1)}
        res = [-1] * len(nums1)

        stack = []

        for i in range(len(nums2)):
            cur = nums2[i]
            while stack and cur > stack[-1]:
                val = stack.pop()
                idx = nums1Idx[val]
                res[idx] = cur
            if cur in nums1Idx:
                stack.append(cur)
        return res
            
        # TC: O(m*n), SC: O(m)

        nums1Idx = {n:i for i, n in enumerate(nums1)} # hashmap
        res = [-1] * len(nums1) # output

        for i in range(len(nums2)):
            if nums2[i] not in nums1Idx:
                continue
            for j in range(i+1, len(nums2)):
                if nums2[j] > nums2[i]:
                    idx = nums1Idx[nums2[i]]
                    res[idx] = nums2[j]
                    break
        return res
            