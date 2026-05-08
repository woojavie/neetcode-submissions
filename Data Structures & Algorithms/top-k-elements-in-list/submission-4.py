class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map = {}
        for n in nums:
            map[n] = 1 + map.get(n, 0)
        countArr = [[] for i in range(len(nums) + 1)]
        for m in map:
            countArr[map[m]].append(m)
        res = []
        for x in range(len(countArr) - 1, 0, -1):
            for num in countArr[x]:
                res.append(num)
                if len(res) == k:
                    return res