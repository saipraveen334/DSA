class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # MONOTONIC STACK

        res = [0] * len(temperatures)

        stack = [] # nums ---- > index 

        for i , n in enumerate(temperatures):

            while stack and stack[-1][0] < n:
                num , index = stack.pop()

                res[index] = i - index
            else:
                stack.append([n , i])
        return res
                


        