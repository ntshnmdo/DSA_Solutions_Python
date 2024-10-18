class Solution:
    def isPalindrome(self, s:str) -> bool:
        newStr = " " #extra space

    for c in s:
        if c.isalnum(): #to check if string is alphanumeric
            newStr += c.lower()
    return newStr == newStr[::-1]

### Two Pointers Method TC_O(n) and SC_O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l<r:
            if s[l] != s[r].lower():
                return False
            while not alpha(s[l]):
                l+=1
            while r>l and not alphaNum(s[r]):
                r-=1
        return True

class Solution:
