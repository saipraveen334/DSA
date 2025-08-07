class Solution {
    public int maxProfit(int[] prices) {
        int MaxProfit = 0 , l = 0 , r = 1 ;

        while(r < prices.length) {
            if (prices[r] > prices[l]) {
                MaxProfit = Math.max( MaxProfit , prices[r] - prices[l]);
            }
            else{
                l = r;
            }
            r++;
        }
        return MaxProfit;
    }
}