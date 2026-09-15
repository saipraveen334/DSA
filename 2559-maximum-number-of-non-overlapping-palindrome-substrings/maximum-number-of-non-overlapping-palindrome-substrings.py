class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        ans = 0
        i = 0

        while i < n:
            found = False

            # Check palindrome of length k
            if i + k <= n:
                left = i
                right = i + k - 1

                while left < right and s[left] == s[right]:
                    left += 1
                    right -= 1

                if left >= right:
                    ans += 1
                    i += k
                    found = True

            # Check palindrome of length k + 1
            if not found and i + k + 1 <= n:
                left = i
                right = i + k

                while left < right and s[left] == s[right]:
                    left += 1
                    right -= 1

                if left >= right:
                    ans += 1
                    i += k + 1
                    found = True

            if not found:
                i += 1

        return ans