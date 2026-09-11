class Solution:
    def totalNumbers(self, digits: List[int]) -> int:

        ans = set()

        def dfs(cur, used):

            if len(cur) == 3:

                if cur[0] != 0 and cur[2] % 2 == 0:
                    num = cur[0] * 100 + cur[1] * 10 + cur[2]
                    ans.add(num)

                return

            for i in range(len(digits)):

                if i in used:
                    continue

                used.add(i)
                cur.append(digits[i])

                dfs(cur, used)

                cur.pop()
                used.remove(i)

        dfs([], set())

        return len(ans)