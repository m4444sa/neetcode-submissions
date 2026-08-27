import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversed=s[::-1]
        c_reversed = ''.join(filter(str.isalnum, reversed))
        c_s=''.join(filter(str.isalnum, s))
        if c_reversed.lower()==c_s.lower(): 
            return True
        else:
            return False
