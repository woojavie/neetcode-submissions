class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minK = max(piles)
        while l <= r:
            m = (l + r) // 2
            time = 0
            for j in range(len(piles)):
                hours = math.ceil(piles[j] / m)
                time += hours
            if time <= h:
                minK = min(minK, m)
                r = m - 1
            else:
                l = m + 1
        return minK
        