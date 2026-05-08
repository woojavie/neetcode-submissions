class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        res = []
        for i in range(len(sortedNums) - 2):
            if i > 0 and sortedNums[i] == sortedNums[i - 1]:
                continue
            l, r = i + 1, len(sortedNums) - 1
            while l < r:
                target = -sortedNums[i]
                sum = sortedNums[l] + sortedNums[r]
                if sum > target:
                    r -= 1
                elif sum < target:
                    l += 1
                else:
                    res.append([sortedNums[i], sortedNums[l], sortedNums[r]])
                    l += 1
                    
                    while l < r and sortedNums[l] == sortedNums[l - 1]:
                        l += 1

        return res