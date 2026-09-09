class Solution:
    def countCommas(self, n: int) -> int:
        # optimal sol

        res = 0
        power = 1000

        while power <= n:
            res += n - power + 1
            power *= 1000

        return res
        