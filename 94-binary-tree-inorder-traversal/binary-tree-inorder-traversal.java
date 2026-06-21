/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {

        // RECURSIVE APPROACH
        // List<Integer> res = new ArrayList<Integer>();
        // inorder(root , res );

        //ITERATIVE APPROACH 

        TreeNode cur = root;
        Deque<TreeNode> stack = new ArrayDeque<>();
        List<Integer> res = new ArrayList<>();

        while(cur != null || !stack.isEmpty())
        {
            while(cur != null)
            {
                stack.push(cur);
                cur = cur.left;
            }
            cur = stack.pop();
            res.add(cur.val);
            cur = cur.right;
        }
        return res;



        

    }
    // private void inorder(TreeNode root , List<Integer> res)
    //     {
    //         if(root == null)
    //         {
    //             return;
    //         }
    //         inorder(root.left , res);
    //         res.add(root.val);
    //         inorder(root.right , res);
    //     }
    // return res;
        
}