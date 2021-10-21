class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        minStock = prices[0]
        
        for i in range(1, len(prices)):
            profit = prices[i] - minStock
            ans = max(profit, ans)
            minStock = min(prices[i], minStock)
        
        
        return ans