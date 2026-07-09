class Solution
{
    public TreeNode removeLeafNodes(TreeNode root, int target)
    {
        if (root == null)
        {
            return null;
        }

        Deque<TreeNode> stack = new ArrayDeque<>();
        Set<TreeNode> visit = new HashSet<>();
        Map<TreeNode, TreeNode> parents = new HashMap<>();

        stack.push(root);
        parents.put(root, null);

        while (!stack.isEmpty())
        {
            TreeNode node = stack.peek();

            if (node.left == null && node.right == null && node.val == target)
            {
                stack.pop();
                TreeNode p = parents.get(node);

                if (p == null)
                {
                    return null;
                }

                if (p.left == node)
                {
                    p.left = null;
                }
                if (p.right == node)
                {
                    p.right = null;
                }
            }
            else if (!visit.contains(node))
            {
                visit.add(node);

                if (node.left != null)
                {
                    stack.push(node.left);
                    parents.put(node.left, node);
                }
                if (node.right != null)
                {
                    stack.push(node.right);
                    parents.put(node.right, node);
                }
            }
            else
            {
                stack.pop();
            }
        }
        return root;
    }
}