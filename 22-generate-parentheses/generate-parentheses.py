class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def dfs(inner , outer):
            if inner == outer == n:
                res.append("".join(stack))
                return 
            

            if inner < n:
                stack.append("(")
                dfs(inner + 1 , outer)
                stack.pop()

            if outer < inner:
                stack.append(")")
                dfs(inner , outer + 1)
                stack.pop()

        dfs(0 , 0)
        return res
