class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]:         # if search space is sorted
                res = min(res, nums[l])   # check leftmost num to see if smaller than res
                break
            m = (l + r) // 2
            res = min(res, nums[m])       # check if current num is smaller than res
            if nums[m] >= nums [l]:       # check if in left sorted portion
                l = m + 1                 # if yes, search right portion
            else:
                r = m - 1                 # if no, search left portion
        return res