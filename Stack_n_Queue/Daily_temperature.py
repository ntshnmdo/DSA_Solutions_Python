class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        results = [0] * len(temperatures) # exact same length as temperatures array # [0] default 0
        stack = [] # extra memory, contains [temp, index] pair

        for i, t in enumerate(temperatures):  # i- index, t - temp, # enumerate is to get(index, value)
            while stack and t > temperatures[stack[-1]]: # t> top value
                index = stack.pop() 
                results[index] = i - index 
            stack.append(i)
        
        return results