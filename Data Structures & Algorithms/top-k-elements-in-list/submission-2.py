class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countmap = {} # value : count
        countarr = [[] for i in range(len(nums) + 1)] # array of list of nums indexed by count
        for n in nums:
            countmap[n] = 1 + countmap.get(n, 0) # mapping number to count
        for key, value in countmap.items(): # looping through keys
            countarr[value].append(key) # adding number to count index
        
        res = []
        for i in range((len(countarr) - 1), 0, -1): # looping through backwards
            for x in countarr[i]:
                res.append(x)   # add number to result array until length of result == k
                if len(res) == k:
                    return res