class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        freq = {}
        res = 0 

        for i in range(len(s) - minSize + 1):
            sub = s[i : i + minSize]

            if (len(set(sub))) <= maxLetters:
                freq[sub] = freq.get(sub , 0) + 1

                res = max(res , freq[sub])
        return res
