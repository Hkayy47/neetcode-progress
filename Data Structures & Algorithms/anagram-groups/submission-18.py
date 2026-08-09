class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        mainmap = {}
        for i, s in enumerate(strs):
            st = s
            s = "".join(sorted(s))
            if s not in mainmap:
                mainmap[s] = [st]
            else:
                mainmap[s].append(st)

        return list(mainmap.values())
            
            
        


                