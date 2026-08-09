class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = ''.join(c.lower() for c in s if c.isalnum())

        j = len(s) - 1
        i = 0
        
        while i < j:
            if s[i] != s[j]:
                return False
            i+= 1
            j -=1

        return True

        