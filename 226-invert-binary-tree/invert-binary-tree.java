class Solution
{
    public TreeNode invertTree(TreeNode root)
    {
        if (root == null)
        {
            return null;
        }

        Queue<TreeNode> q = new LinkedList<>();
        q.add(root);

        while (!q.isEmpty())
        {
            TreeNode node = q.poll();

            TreeNode temp = node.left;
            node.left = node.right;
            node.right = temp;

            if (node.left != null)
            {
                q.add(node.left);
            }
            if (node.right != null)
            {
                q.add(node.right);
            }
        }
        return root;
    }
}