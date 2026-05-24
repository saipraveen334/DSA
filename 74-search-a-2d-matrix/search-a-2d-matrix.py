class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # GETTING ROW AND THEN SEARCHING THE COLUMNS OF THAT ROW 

        Rows , Cols = len(matrix) , len(matrix[0])

        top = 0 
        bot = Rows - 1

        while top <= bot:
            row = (top + bot ) // 2

            if matrix[row][0] > target:
                bot = row - 1
            elif matrix[row][Cols - 1] < target:
                top = row + 1
            else:
                break
        
        if not (top <= bot):
            return False
        
        l = 0 
        r = Cols -1 
        

        while l <= r:
            m = (l + r) // 2

            if matrix[row][m] > target:
                r = m - 1
            elif matrix[row][m] < target:
                l = m + 1
            else:
                return True
        return False



        