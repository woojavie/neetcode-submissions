class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # start at middle
        # check if bigger or smaller
        l, m , h = 0, len(nums) // 2 , len(nums) - 1
        while h - l >= 0:
            if target > nums[m]:
                l = m + 1
                m = h - ((h - l) // 2)
            elif target < nums[m]:
                h = m - 1
                m = l + ((h - l) // 2)
            else:
                return m
        return -1