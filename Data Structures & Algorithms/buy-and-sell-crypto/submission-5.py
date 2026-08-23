class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_buy = prices[0]

        for p in prices:
            max_profit = max(max_profit, p - min_buy)
            min_buy = min(min_buy, p)
        
        return max_profit