class solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        str1 = backspaceStack(s)
        str2 = backspaceStack(t)

        if str1 != str2:
            return False
        return True
    
def backspaceStack(s):
    stack = []
    for i in s:
        if i != "#":
            stack.append(i)
        else:
            if len(stack) > 0:
                stack.pop()
    return stack

# TC: O(n+m) 
# SC: O(1)