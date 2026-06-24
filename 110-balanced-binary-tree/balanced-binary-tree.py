# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height(cur):
            if not cur:
                return 0 
            
            return 1 + max(height(cur.left) , height(cur.right))

        def dfs(cur):

            if not cur:
                return  True  
            
            left = height(cur.left)
            right = height(cur.right)

            if abs(left - right) > 1:
                return False

            return dfs(cur.left) and dfs(cur.right)
        return dfs(root)
        
        
            
            
        