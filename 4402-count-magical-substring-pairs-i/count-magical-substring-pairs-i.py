class Solution:
    def countMagicalPairs(self, s: str) -> int:
        n = len(s)
        distinct = [[0] * n for _ in range(n)]

        for i in range(n):
            seen = set()
            for j in range(i, n):
                seen.add(s[j])
                distinct[i][j] = len(seen)

        res = 0

        for j in range(n - 1):
            left = [0] * 27
            right = [0] * 27

            for i in range(j + 1):
                left[distinct[i][j]] += 1

            for k in range(j + 1, n):
                right[distinct[j + 1][k]] += 1

            for d in range(1, 27):
                res += left[d] * right[d]

        return res