class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):

            if s[i] != "]":
                stack.append(s[i])

            else:
                # TAKE THE SUBSTRING 

                st = ""

                while stack and stack[-1] != "[":

                    st = stack.pop() + st
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k 
                res = ""

                res = (int(k) * st)
                stack.append(res)
        return "".join(stack)



        