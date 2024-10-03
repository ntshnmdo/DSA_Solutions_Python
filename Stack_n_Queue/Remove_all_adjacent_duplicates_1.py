class solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        ans = ""

        for i in range(len(s)):
            if len(stack) == 0:
                stack.append(s[i])

            elif stack[-1] == s[i]:
                stack.pop()

            else:
                stack.append(s[i])
            
        while len(stack) > 0:
            ans += stack[-1]
            stack.pop()
        return ans[::-1]