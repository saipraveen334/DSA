class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        diff = [abs(a - b) for a, b in zip(nums1, nums2)]
        k = k1 + k2

        if sum(diff) <= k:
            return 0

        freq = [0] * (max(diff) + 1)

        for x in diff:
            freq[x] += 1

        mx = max(diff)

        while k > 0 and mx > 0:
            while mx > 0 and freq[mx] == 0:
                mx -= 1

            if mx == 0:
                break

            count = freq[mx]
            operations = min(k, count)

            freq[mx] -= operations
            freq[mx - 1] += operations
            k -= operations

        return sum(i * i * count for i, count in enumerate(freq))