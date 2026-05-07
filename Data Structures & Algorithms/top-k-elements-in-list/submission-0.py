class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countmap = {} # value : count
        countarr = [[] for i in range(len(nums) + 1)]
        for n in nums:
            countmap[n] = 1 + countmap.get(n, 0)
        for key, value in countmap.items():
            countarr[value].append(key)
        
        res = []
        for i in range((len(countarr) - 1), 0, -1):
            for x in countarr[i]:
                res.append(x)
                if len(res) == k:
                    return res