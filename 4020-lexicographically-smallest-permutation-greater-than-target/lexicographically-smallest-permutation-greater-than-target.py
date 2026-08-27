from collections import Counter

class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:

        n = len(target)
        count = Counter(s)
        prefixMatch = True
        res = []

        for i in range(n):

            if prefixMatch:

                current = target[i]
                used = False

                if count[current] > 0:
                    count[current] -= 1
                    used = True

                    test = [current]

                    for k, v in sorted(count.items(), reverse=True):
                        test.append(k * v)

                    if "".join(res + test) > target:
                        res.append(current)
                        continue

                if used:
                    count[current] += 1

                current = chr(ord(current) + 1)

                while current <= "z" and count[current] == 0:
                    current = chr(ord(current) + 1)

                if current > "z":
                    return ""

                count[current] -= 1
                res.append(current)
                prefixMatch = False

            else:

                for k, v in sorted(count.items()):
                    res.append(k * v)

                return "".join(res)

        if not prefixMatch:
            for k, v in sorted(count.items()):
                res.append(k * v)

            return "".join(res)

        return ""