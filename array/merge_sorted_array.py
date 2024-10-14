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