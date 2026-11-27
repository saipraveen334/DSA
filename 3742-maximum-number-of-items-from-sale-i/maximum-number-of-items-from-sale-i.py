class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        min_price = min(price for factor, price in items)

        dp = [-float('inf')] * (budget + 1)
        dp[0] = 0

        for factor, price in items:
            count = sum(f % factor == 0 for f, p in items)

            for j in range(budget, price - 1, -1):
                dp[j] = max(dp[j], dp[j - price] + count)

        return max(
            dp[j] + (budget - j) // min_price
            for j in range(budget + 1)
        )