def isAnagram(self, s:str, t:str) -> bool:
    if len(s) != len(t):
        return False
    
    countS, countT = {}, {} # we are creating hash maps for s and t string

    for i in range(len(s)):     # now if len(s) = len(t), we can iterate in any str s or t.
        countS[s[i]] = 1 + countS.get(s[i], 0)  # here we are using get function which basically return 0 if the next letter doesnt exist.
        countT[t[i]] = 1 + countT.get(t[i], 0)   # this is building of the hash maps
    for c in countS:
        if countS[c] != countT.get(c, 0):  # here we are checking the condition.
            return False
        
    return True
          
# 2nd Solution , There exist fuction in python to make it one line code, but that doesnt work in interview.
# return counter(s) == counter(t) 
# Time and space complexity of both the code are same 
# if interviewer ask if you can solve this ques with O(1) memory
# we will use sorted function 
# return sorted(s) == sorted(t)

