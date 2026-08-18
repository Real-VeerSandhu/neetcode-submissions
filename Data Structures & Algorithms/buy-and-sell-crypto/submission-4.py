class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        minBuy = prices[0]

        for sell in prices:
            maxP = max(maxP, sell - minBuy) # sell today
            minBuy = min(minBuy, sell) # buy today
        
        return maxP