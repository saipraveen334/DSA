public class Codec
{
    public String serialize(TreeNode root)
    {
        StringBuilder res = new StringBuilder();
        dfsSerialize(root, res);
        return res.toString();
    }

    private void dfsSerialize(TreeNode node, StringBuilder res)
    {
        if (node == null)
        {
            res.append("N,");
            return;
        }

        res.append(node.val).append(",");
        dfsSerialize(node.left, res);
        dfsSerialize(node.right, res);
    }

    public TreeNode deserialize(String data)
    {
        String[] vals = data.split(",");
        int[] index = {0};
        return dfsDeserialize(vals, index);
    }

    private TreeNode dfsDeserialize(String[] vals, int[] index)
    {
        if (vals[index[0]].equals("N"))
        {
            index[0]++;
            return null;
        }

        TreeNode node = new TreeNode(Integer.parseInt(vals[index[0]]));
        index[0]++;

        node.left  = dfsDeserialize(vals, index);
        node.right = dfsDeserialize(vals, index);

        return node;
    }
}