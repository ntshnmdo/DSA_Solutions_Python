# Sorting TC_O(nlogn) SC_O(1)
def isAnagram(self, s:str, t:str) -> bool:
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

# Hash Table SC_O(1) and TC_O(n)
 
def isAnagram(self, s:str, t:str) -> bool:
    if len(s) != len(t):
        return False
    
    countS, countT = {}, {} # we are creating hash maps for s and t string

    for i in range(len(s)):     # now if len(s) = len(t), we can iterate in any str s or t.
        countS[s[i]] = 1 + countS.get(s[i], 0)  # here we are using get function which basically return 0 if the next letter doesnt exist.
        countT[t[i]] = 1 + countT.get(t[i], 0)   # this is building of the hash maps
    for c in countS:
        if countS[c] != countT.get(c, 0):  # here we are checking the condition. Iterating through hashmaps
            return False  # or directly write - return countS == countT
        
    return True
          
# 2nd Solution , There exist fuction in python to make it one line code, but that doesnt work in interview.
# return Counter(s) == Counter(t)  # it is a hashmap in python 
# Time and space complexity of both the code are same 
# if interviewer ask if you can solve this ques with O(1) memory
# we will use sorted function 
# return sorted(s) == sorted(t)

# Hash Table (Optimal) TC_O(n) and SC_O(1)

def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    count = [0] * 26

    for i in range(len(s)):
        count[ord(s[i]) - ord('a')] += 1
        count[ord(t[i]) - ord('a')] -= 1
    
    for val in count:
        if val != 0:
            return False
        
    return True
