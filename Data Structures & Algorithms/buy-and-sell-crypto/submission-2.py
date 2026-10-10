class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        left = 0
        right = 1
        bestProfit = 0
        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit < 0:
                left=right
                continue
            else:
                bestProfit = max(bestProfit, profit)

            right+=1
        

        return bestProfit