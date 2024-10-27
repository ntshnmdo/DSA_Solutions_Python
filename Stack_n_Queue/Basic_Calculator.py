class Solution:
    def calculator(self, s: str) -> int:
        curr = res = 0
        sign = 1
        stack = []

        for char in s:
            if char.isdigit():
                curr = curr * 10 + int(char) # to handle big numbers 334, 34, etc
            elif char in ['+', '-']:
                res += sign * curr

                sign = 1 if char == '+' else -1

                curr = 0 # reset curr to 0 as we get sign
            elif char == "(":
                stack.append(res)
                stack.append(sign)

                sign = 1 # reset

                res = 0 # reset 
            elif char == ")":
                res += sign * curr

                res *= stack.pop()

                res += stack.pop()

                curr = 0
        
        return res + sign * curr
    
# TC: O(n)
# SC: O(n)