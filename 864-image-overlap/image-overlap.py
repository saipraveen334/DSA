class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        count = collections.defaultdict(int)
        ans = 0

        for r1 in range(n):
            for c1 in range(n):
                if img1[r1][c1] == 0:
                    continue

                for r2 in range(n):
                    for c2 in range(n):
                        if img2[r2][c2] == 0:
                            continue

                        dr = r2 - r1
                        dc = c2 - c1

                        count[(dr, dc)] += 1
                        ans = max(ans, count[(dr, dc)])

        return ans