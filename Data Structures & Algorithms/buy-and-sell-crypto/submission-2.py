class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum= prices[0]
        profit= 0
        for price in range(1, len(prices)):
            if minimum < prices[price]:
                profit_c= prices[price]- minimum
                if profit_c > profit:
                    profit= profit_c
            else:
                minimum= prices[price]
        return profit