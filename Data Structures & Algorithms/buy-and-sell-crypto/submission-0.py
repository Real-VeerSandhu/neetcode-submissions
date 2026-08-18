class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        maxProfit =0

        if (len(prices) == 1):
            profit = 0
            return profit

        left = 0
        right = 1

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit, profit)
            else:
                left = right
            right += 1
        return maxProfit


        