class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ma = 0
        t = prices[0]
        for i in range(1, len(prices)):
            p = 0
            if  t < prices[i]:
                p = prices[i]-t
            else:
                t = prices[i]
            ma = max(p, ma)
        return ma

        