class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hashmp = {}
        n, m = len(s1), len(s2)
        if n > m:
            return False
        for c in s1:
            hashmp[c] = hashmp.get(c, 0) + 1
        n = len(s1)
        copy = hashmp.copy() 
        r = 0
        count = n  
        while r < len(s2):
            if s2[r] in hashmp:
                if hashmp[s2[r]] > 0:
                    count-=1
                hashmp[s2[r]]-=1
            if r >= len(s1):
                l = r - n
                if s2[l] in hashmp:
                    hashmp[s2[l]] += 1
                    if hashmp[s2[l]] > 0:
                        count += 1 
            r+=1
            if count == 0:
                return True


        
        

        return False
            


        