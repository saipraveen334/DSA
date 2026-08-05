class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = []
        cur = []
        wordDict = set(wordDict)

        # i being pointed the current index of string s 
        def backtrack(i):
            if i == len(s):
                res.append(" ".join(cur))
                return 
            
            for j in range(i , len(s)):
                if s[i : j + 1] in wordDict:
                    cur.append(s[i : j + 1])

                    backtrack(j + 1)

                    cur.pop()
        backtrack(0)
        return res




        