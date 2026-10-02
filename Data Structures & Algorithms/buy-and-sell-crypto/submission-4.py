class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        start = 0
        maxprofit = 0
        startprices = prices[0:len(prices)-1]
        for price in startprices:
            maxprofit = max(max(prices[start:len(prices)]) - price, maxprofit)
            start += 1 
            print(f"max this iteration {max(prices[start:len(prices)])}") 
        return maxprofit
