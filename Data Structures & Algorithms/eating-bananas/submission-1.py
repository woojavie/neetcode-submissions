class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minK = max(piles)
        while l <= r:
            k = (l + r) // 2
            total = 0
            for n in piles:
                total += math.ceil(n/k)
            if total > h:
                l = k + 1
            else:
                minK = min(k, minK)
                r = k - 1
        return minK
            
            