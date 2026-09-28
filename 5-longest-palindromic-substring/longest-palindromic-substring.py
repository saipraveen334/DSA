class Solution:
    def longestPalindrome(self, s: str) -> str:
        reslen = 0
        resInd = 0

        for i in range(len(s)):

            # odd length
            l = i
            r = i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if reslen < r - l + 1:
                    reslen = r - l + 1
                    resInd = l

                l -= 1
                r += 1

            # even length
            l = i
            r = i + 1

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if reslen < r - l + 1:
                    reslen = r - l + 1
                    resInd = l

                l -= 1
                r += 1

        return s[resInd:resInd + reslen]