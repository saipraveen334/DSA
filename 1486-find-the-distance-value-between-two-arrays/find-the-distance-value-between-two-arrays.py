class Solution:
    def findTheDistanceValue(self, arr1: list[int], arr2: list[int], d: int) -> int:
        count = 0

        for n1 in arr1:
            flag = False

            for n2 in arr2:
                if abs(n1 - n2) > d:
                    flag = True 
                else:
                    flag = False
                    break 
            
            if flag:
                count += 1
                
        return count


        