class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # backtracking with memoization  
        memo = {}

        wordDict = set(wordDict)  # just avoiding dulpicates
        def dfs(i):

            # base case 
            if i == len(s):
                return True 

            # memoization 
            if i in memo:
                return memo[i]

            for j in range(i , len(s) + 1):
                if s[i : j + 1] in wordDict:
                    if dfs(j + 1):
                        memo[i] = True 
                        return True
            
            memo[i] = False 
            return False 
        return dfs(0)


        # backtracking brute force method 
        wordDict = set(wordDict)

        def dfs(i):
            if i == len(s):
                return True 
            
            for j in range(i ,len(s) + 1):

                if s[i : j + 1] in wordDict:
                    if dfs(j + 1):
                        return True 
            return False

        return dfs(0)


            