class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        rec1={}
        rec2={}
        for char in s:
            rec1[char] = rec1.get(char, 0) + 1
        for char in t:
            rec2[char] = rec2.get(char, 0) + 1
        if rec1==rec2: 
            return True
        else: 
            return False