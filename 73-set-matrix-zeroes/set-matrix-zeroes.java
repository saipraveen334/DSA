class Solution {
    public void setZeroes(int[][] matrix) {
        int rows = matrix.length ;
        int cols = matrix[0].length ;

        boolean[] row = new boolean[rows] ;
        boolean[] col = new boolean[cols] ;

        for(int i = 0 ; i < rows ; i ++)
        {
            for(int j = 0; j < cols ; j++)
            {
                if (matrix[i][j] == 0 )
                {
                    row[i] = true;
                    col[j] = true;
                }
            }
        }
        for(int r = 0 ; r < rows ; r ++)
        {
            for(int c = 0 ; c < cols ; c++)
            {
                if (row[r] || col[c])
                {
                    matrix[r][c] = 0 ;
                }
            }
        }
        
    }
}