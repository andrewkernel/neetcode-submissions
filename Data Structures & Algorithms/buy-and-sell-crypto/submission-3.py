class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        for i in range((len(prices))):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices[i]
                output = max(output, profit)
        return output

        