class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        best = [0] * k
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        values = []
        for num in dic:
            values.append((num, dic[num]))
        
        values.sort(key = lambda x: -x[1])

        for i in range(k):
            best[i] = values[i][0]
        
        return best



            


        