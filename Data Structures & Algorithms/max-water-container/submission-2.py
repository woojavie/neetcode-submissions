class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxA = 0

        while l < r:
            area = (r - l) * min(heights[r], heights[l])
            maxA = max(area, maxA)
            if heights[r] < heights[l]:
                r -= 1
            elif heights[r] > heights[l]:
                l += 1
            else:
                r -= 1
        return maxA
