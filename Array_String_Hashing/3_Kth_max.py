def kth_Max(self, nums, l, r, k):
    nums.sort()
    return nums[len(nums) - k]