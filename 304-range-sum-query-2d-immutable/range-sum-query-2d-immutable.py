class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows , cols = len(matrix) , len(matrix[0])

        self.NewMatrix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for r in range(rows):
            prefix = 0
            for c in range(cols):
                prefix += matrix [r][c]

                above = self.NewMatrix[r][c + 1]
                self.NewMatrix[r + 1][c + 1]= prefix + above
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 += 1
        col1 += 1
        row2 += 1
        col2 += 1

        bottomright = self.NewMatrix[row2][col2]
        topleft = self.NewMatrix[row1-1][col1-1]
        left = self.NewMatrix[row2][col1-1]
        above = self.NewMatrix[row1-1][col2]

        return bottomright - left - above + topleft

        
