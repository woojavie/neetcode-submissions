class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        res = []
        for i in range(len(sortedNums)):
            if i > 0 and sortedNums[i] == sortedNums[i - 1]:
                continue
            j,k = i + 1, len(sortedNums) - 1
            target = -sortedNums[i]
            while j < k:
                total = sortedNums[j] + sortedNums[k]
                if total > target:
                    k -= 1
                elif total < target:
                    j += 1
                else:
                    res.append([sortedNums[i], sortedNums[j], sortedNums[k]])
                    j += 1
                    while j < k and sortedNums[j] == sortedNums[j - 1]:
                        j += 1
        return res
            