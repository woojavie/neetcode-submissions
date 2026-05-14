class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[l]

        while l <= r:
            if nums[l] < nums[r]:
                res = min(nums[l], res)
            m = (l + r) // 2
            if nums[m] < nums[r]:
                res = min(nums[m], res)
                r = m - 1
            else:
                res = min(nums[m], res)
                l = m + 1
        return res