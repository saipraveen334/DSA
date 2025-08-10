class Solution {
    public int[] diStringMatch(String s) 
    {
        int n = s.length();
        int[] ans = new int[n + 1];

        int low = 0, high = n, idx = 0;

        for (int i = 0; i < n; i++) 
        {
            if (s.charAt(i) == 'I')
            { 
                ans[idx++] = low++;
            }
            else 
            {
                ans[idx++] = high--;
            }
        }
        ans[idx] = low;
        return ans;
    }
}
