class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int rows = matrix.length ;
        int cols = matrix[0].length ;
        int left = 0 ;
        int right = cols ;
        int top = 0 ;
        int bottom = rows ;
        List<Integer> res = new ArrayList<>();
        int idx = 0; 

        while (left < right &&  top < bottom)
        {
            //  FROM LEFT TO RIGHT
            for(int i = left ; i < right ; i++ )
            {
                res.add(matrix[top][i]) ;
            }
            top ++ ;

            //  FROM TOP TO BOTTOM 

            for(int i = top ; i < bottom ; i ++)
            {
                res.add(matrix[i][right-1]) ;
            }
            right -- ;

            if (!(left < right && top < bottom))
            {
                break ;
            }

            // FROM RIGHT TO LEFT 

            for(int i = right - 1; i >= left ; i--)
            {
                res.add(matrix[bottom - 1][i]) ;
            }
            bottom --;
            
            // FROM BOTTOM TO TOP 

            for(int i = bottom - 1 ; i >= top ; i-- )
            {
                res.add(matrix[i][left]) ;
            }
            left += 1 ;
            
        }
        return res;
        


        
    }
}