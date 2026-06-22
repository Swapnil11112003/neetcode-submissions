class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 1
        max_diff = 0
        while j < len(prices):
            diff = prices[j] - prices[i]
            if prices[j] < prices[i]:
                i = j
            j += 1
            max_diff = max(diff, max_diff)

        return max_diff
