class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """Return the shortest substring of s containing every char of t with multiplicity."""
        if not t or len(s) < len(t):
            return ""

        need: dict[str, int] = {}
        for c in t:
            need[c] = need.get(c, 0) + 1

        count = len(t)          # units of t still missing from the window
        best_len = len(s) + 1   # sentinel: one past any legal window length
        best_l = 0
        l = 0

        for r, c in enumerate(s):
            if c in need:
                if need[c] > 0:     # this occurrence fills a real gap
                    count -= 1
                need[c] -= 1        # may go negative = surplus in window

            while count == 0:       # window is valid; shrink while it stays valid
                if r - l + 1 < best_len:
                    best_len = r - l + 1
                    best_l = l
                left = s[l]
                if left in need:
                    need[left] += 1
                    if need[left] > 0:   # removing it opened a real gap
                        count += 1
                l += 1

        return "" if best_len > len(s) else s[best_l:best_l + best_len]