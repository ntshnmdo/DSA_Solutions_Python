def twosum(self, nums: list[int], target: int) -> list[int]:
    prevMap = {} # this is hashmap, val : index

    for i, n in enumerate(nums): # Enumerate is a built-in function in python that allows you to keep track of the number of iterations (loops) in a loop. 
        # This enumerate object contains a count (from the start, which always defaults to 0) and a value obtained from iterating over the iterable object.
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff], i]
        prevMap[n] = i
    return

l = [2,1,3,4]
t = 5
print(twosum(l,t))