class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # value : count
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        countArr = [[] for i in range(len(nums) + 1)]
        res = []
        for key in count:
            countArr[count[key]].append(key)
        for n in range(len(countArr) - 1, 0, -1):
            for x in countArr[n]:
                res.append(x)
                if len(res) == k:
                    return res