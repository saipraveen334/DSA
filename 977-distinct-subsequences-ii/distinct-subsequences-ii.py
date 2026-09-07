class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7

        dp = [0] * 26

        for ch in s:
            idx = ord(ch) - ord('a')

            total = sum(dp) % MOD

            # All existing distinct subsequences + current character
            dp[idx] = (total + 1) % MOD

        return sum(dp) % MOD