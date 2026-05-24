class Solution
{
    public boolean searchMatrix(int[][] matrix, int target)
    {
        int rows = matrix.length;
        int cols = matrix[0].length;

        int top = 0;
        int bot = rows - 1;
        int row = 0;

        while (top <= bot)
        {
            row = (top + bot) / 2;

            if (matrix[row][0] > target)
            {
                bot = row - 1;
            }
            else if (matrix[row][cols - 1] < target)
            {
                top = row + 1;
            }
            else
            {
                break;
            }
        }

        if (!(top <= bot))
        {
            return false;
        }

        int l = 0;
        int r = cols - 1;

        while (l <= r)
        {
            int mid = l + (r - l) / 2;

            if (matrix[row][mid] > target)
            {
                r = mid - 1;
            }
            else if (matrix[row][mid] < target)
            {
                l = mid + 1;
            }
            else
            {
                return true;
            }
        }
        return false;
    }
}