class Solution
{
    int res;

    public int maxPathSum(TreeNode root)
    {
        res = root.val;
        dfs(root);
        return res;
    }

    private int dfs(TreeNode root)
    {
        if (root == null)
        {
            return 0;
        }

        int left  = dfs(root.left);
        int right = dfs(root.right);

        int leftMax  = Math.max(left, 0);
        int rightMax = Math.max(right, 0);

        res = Math.max(res, root.val + leftMax + rightMax);

        return root.val + Math.max(leftMax, rightMax);
    }
}