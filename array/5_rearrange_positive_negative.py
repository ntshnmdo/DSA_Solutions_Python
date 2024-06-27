class Solution:
    def rearrange(self, arr, n):
        l, r = 0, n-1

        while l < r:
            if arr[l] < 0 and arr[r] > 0:
                l += 1
                r -= 1
            elif arr[l] > 0 and arr[r] < 0:
                arr[l], arr[r] == arr[r], arr[l]
                l += 1
                r -= 1
            elif arr[l] > 0 and arr[r] > 0:
                r -= 1
            elif arr[l] < 0 and arr[r] < 0:
                l += 1
            
            