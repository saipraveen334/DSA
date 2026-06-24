# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        #DFS 
        def dfs(root):
            if not root:
                return [True , 0]

            left  = dfs(root.left) 
            right = dfs(root.right)

            Balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1


            return [Balanced , 1 + max(left[1] , right[1])]
        return dfs(root)[0]


        #BRUTE FORCE 
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
        
        
            
            
        