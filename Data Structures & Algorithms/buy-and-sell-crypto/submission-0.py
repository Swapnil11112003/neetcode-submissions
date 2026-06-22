class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        i = 0
        for j in range(len(prices)):
            prices_i = prices[i]
            prices_j = prices[j]

            if prices_j < prices_i:
                i = j
                continue

            cur_profit = prices_j - prices_i
            if cur_profit > max_profit:
                max_profit = cur_profit
                
        return max_profit

            

            
    
