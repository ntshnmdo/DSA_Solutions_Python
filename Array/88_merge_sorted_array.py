# Two-Pointer method: TC_O(m+n), SC_O(1)

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        i = m - 1
        j = n - 1
        k = m + n - 1

        while j>=0:
            if i>=0 and nums1[i]>nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

# TC_O((m+n)log(m+n)) and SC_O(1)

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        for j in range(n):
            nums1[m+j] = nums2[j]
        nums1.sort()

# Best, TC O(m=n) and SC O(1) 

class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        # get the last index of nums1
        last = m+n-1

        # merge them in reverse order

        while m>0 and n>0: # while elements left in both the array
            if nums1[m-1] > nums2[n-2]:
                nums1[last] = nums1[m-1]
                m-=1
            else:
                nums1[last] = nums2[n-1]
                n-=1
            last -= 1

        # fill nums1 with leftover elements in nums2 elements
        while n>0:
            nums1[last] = nums2[n-1]
            n, last = n-1, last-1
