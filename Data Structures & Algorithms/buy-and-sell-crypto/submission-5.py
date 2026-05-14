class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, len(prices) - 1
        res = 0
        minBuy = prices[0]
        for i in range(len(prices)):
            minBuy = min(prices[i], minBuy)
            profit = prices[i] - minBuy
            res = max(res, profit)
        return res