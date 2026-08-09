class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for x in strs:
            ans+=x
            ans+="<>"
        return ans

    def decode(self, s: str) -> List[str]:
        st = ""
        ans = []
        for c in s:
            if c != "<":
                if c != ">":
                    st+=c
            else:
                ans.append(st)
                st = ""
        return ans
