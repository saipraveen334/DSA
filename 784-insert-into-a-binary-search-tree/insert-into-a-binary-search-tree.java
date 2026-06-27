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
    public TreeNode insertIntoBST(TreeNode root, int val) {
        // ITERATIVE VERSION 
        // BASE CASE 

        if(root == null)
        {
            return new TreeNode(val);
        }

        TreeNode cur = root;

        while(true)
        {
            if(val > cur.val)
            {
                if(cur.right == null)
                {
                    cur.right = new TreeNode(val);
                    break;
                }
                cur = cur.right;
            }
            else
            {
                if(cur.left == null)
                {
                    cur.left = new TreeNode(val);
                    break;
                }
                cur = cur.left; 
            }
        }
        return root;
    }
}
        
        
        //RECURSIVE VERSION 

//         if(root == null)
//         {
//             return new TreeNode(val);
//         }

//         if(val > root.val)
//         {
//             root.right = insertIntoBST( root.right, val);
//         }
//         else
//         {
//             root.left = insertIntoBST(root.left , val);
//         }
//         return root;
        
//     }
// }