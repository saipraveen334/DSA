class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l = 0
        n = len(cardPoints)
        total = sum(cardPoints)
        window = sum(cardPoints[:n-k])
        cursum = total - window

        for r in range(n - k , n):
            window = window - cardPoints[l] + cardPoints[r]
            cursum = max(cursum , total - window )
            l += 1
        return cursum


            




        