class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        cheapest = min(price for _, price in items)
        dp = [money // cheapest for money in range (budget+1)]
        for i in range(n):
            factor,price = items[i]
            if price>budget:
                continue
            gain = 1
            for j in range(n):
                if j!=i and items [j][0]%factor == 0:
                    gain+=1
            for money in range(budget,price-1,-1):
                dp[money] = max(dp[money],dp[money-price]+gain)
        return dp[budget]
        
        