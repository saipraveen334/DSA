class NumMatrix {
    private int[][] newMat;

    public NumMatrix(int[][] matrix) {
        int rows = matrix.length ;
        int cols = matrix[0].length ;

        newMat = new int[rows + 1][cols + 1];

        for(int r = 0 ; r < rows ; r ++)
        {
            int prefix = 0 ;

            for (int c = 0 ; c < cols ; c++)
            {
                int above = newMat[r][c + 1] ;
                prefix += matrix[r][c] ;
                newMat[r + 1][c + 1] = above + prefix ;
            }
        } 
        
    }
    
    public int sumRegion(int row1, int col1, int row2, int col2) {
        row1++ ;
        row2++ ;
        col1++ ;
        col2++ ;

        int bottomright = newMat[row2][col2] ;
        int bottomleft = newMat[row2][col1 - 1];
        int topleft = newMat[row1 -1][col1 -1] ;
        int topright = newMat[row1-1][col2];

        return bottomright - bottomleft - topright + topleft ;


    }
}

/**
 * Your NumMatrix object will be instantiated and called as such:
 * NumMatrix obj = new NumMatrix(matrix);
 * int param_1 = obj.sumRegion(row1,col1,row2,col2);
 */