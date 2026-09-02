import math

class Solution:
    def largestString(self, nums: list[int]) -> list[str]:

        def maxStr(n):
            result = []

            while n > 0:

                power = int(math.log2(n))

                if power > 25:
                    result.append("z")
                    n -= 2 ** 25
                else:
                    result.append(chr(ord('a') + power))
                    n -= 2 ** power

            return "".join(result)

        return [maxStr(n) for n in nums]