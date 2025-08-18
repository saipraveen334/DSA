class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        int rows = mat.length ;
        int cols = mat[0].length ;

        int[] res = new int[rows * cols];

        boolean up = true ;
        int idx = 0 , cur_row = 0 , cur_col = 0; 


        while( idx < rows * cols)
        {
            if(up)
            {
                while (cur_row >= 0 && cur_col < cols)
                {
                    res[idx++] = mat[cur_row][cur_col] ;

                    cur_row -- ;
                    cur_col ++ ;
                }
                if (cur_col == cols)
                {
                    cur_row += 2 ;
                    cur_col -= 1 ;
                }
                else
                {
                    cur_row += 1 ;
                }
                up = false ;


            }
            else
            {
                while(cur_row < rows && cur_col >= 0)
                {
                    res[idx++] = mat[cur_row][cur_col] ;

                    cur_row += 1 ;
                    cur_col -= 1 ;
                }
                if(cur_row == rows)
                {
                    cur_col += 2 ;
                    cur_row -= 1 ;
                }
                else
                {
                    cur_col += 1 ;
                }
                up = true ;
            } 

        }
        return res; 
        
    }
}