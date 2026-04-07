import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = self.removeNonAlphaNumeric(s)
        half = len(s)//2
        for i in range(half):
            if s[i] != s[len(s)-i-1]:
                return False
        
        return True
        

    def removeNonAlphaNumeric(self, st: str) -> str:
        st = st.lower()
        st = re.sub(r'[^a-zA-Z0-9]', '', st)
        return st