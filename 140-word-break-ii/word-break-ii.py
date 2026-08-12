class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        # Backtracking with memoization
        res = []
        cache = {}

        def backtrack(i):
            if i == len(s):
                return [""]
            
            if i in cache:
                return cache[i]


            res = []

            for j in range( i , len(s)):

                w = s[i : j + 1]

                if w not in wordDict:
                    continue 

                strings = backtrack(j + 1)

                for subs in strings:
                    sentence = w

                    if subs:
                        sentence += " " + subs
                    res.append(sentence)
            cache[i] = res 
            return res
        return backtrack(0)    

        # Backtracking algo 

        cur = []
        res = []
        wordDict = set(wordDict)

        def backtrack(i):
            if i == len(s):
                res.append(" ".join(cur))
                return 
            
            for j in range( i , len(s)):
                w = s[i : j + 1]  # python is inclusive

                if w in wordDict:
                    cur.append(w)
                    backtrack( j + 1)
                    cur.pop()
        backtrack(0)
        return res 
            




        