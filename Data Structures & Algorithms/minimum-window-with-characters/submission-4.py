class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        n = len(s)
        myst = deque()
        mp = {}
        for c in t:
            mp[c] = mp.get(c, 0) + 1
        ans = ""
        mini = len(s) + 1
        count = len(t)
        l, r = 0, 0
        while r < len(s):
            myst.append(s[r])            
            if s[r] in mp:
                if mp[s[r]] > 0:
                    count-=1
                mp[s[r]] -= 1
            while count == 0:
                st = s[l:r + 1]
                if len(st) < mini:
                    mini = len(st)
                    ans = st
                myst.popleft()
                if s[l] in mp:
                    mp[s[l]] += 1
                    if mp[s[l]] > 0:
                        count+=1
                l+=1
            r+=1
            
        return ans


        