class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        left, right = 0, 1 # Left -> Buy, Right -> Sell
        maxP = 0 # Profit -> Sell - Buy

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxP = max(maxP, profit)
            else:
                left = right
            right += 1
        
        return maxP