# [0,0,1,1,1,2,2,3,3,4]
# l is left, r is right
def nums():
    if len(nums) == 0:
        return 0
    
    j = 0 # starting from 0 
    
    for i in range(1, len(nums)): # r will go to all the length  
        if nums[i] != nums[j]: # comparing with previous value
            j += 1
            nums[j] = nums[i] # so if we get new unique value, we put it in wherever our l value is .
        # increasing the left pointer
    return j+1