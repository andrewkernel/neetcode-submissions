class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        maxP = 0

        for end in range(1, len(prices)):
            if prices[end] < prices[start]:
                start = end
            else:
                profit = prices[end] - prices[start]
                maxP = max(maxP, profit)
        return maxP
            
        