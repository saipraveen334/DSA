class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for c in s:
            if c == ")":
                temp = ""

                while stack and stack[-1] != "(":
                    temp += stack.pop()

                stack.pop()

                for c in temp:
                    stack.append(c)
            else:
                stack.append(c)

        return "".join(stack)