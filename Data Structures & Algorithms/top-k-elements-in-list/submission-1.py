class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap to count the number of occurences
        count = {} # value : count
        for n in nums:
            count[n] = 1 + count.get(n,0)
        countarr = [[] for item in range(len(nums) + 1)]
        for x in count:
            countarr[count[x]].append(x) # array of array of nums indexed by count
        # bucket sort to map array index to list of numbers
        res = []
        for i in range(len(countarr) - 1, 0, -1):
            for num in countarr[i]:
                res.append(num)
                if len(res) == k:
                    return res
        # iterate from back of list and add to result list until length == k