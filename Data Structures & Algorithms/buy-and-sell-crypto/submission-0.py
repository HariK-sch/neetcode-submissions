class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = math.inf
        
        profit = 0

        for num in prices:
            lowest = min(lowest, num)

            profit = max(num - lowest, profit)

        return profit