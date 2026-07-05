# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #INORDER TRAVERSAL ITERATIVE METHOD

        res = []
        stack = []
        cur = root 

        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val

            cur = cur.right
        
            


        #INORDER TRAVERSAL 
        res = []

        def dfs(node):

            # BASE CASE 
            if not node:
                return 

            dfs(node.left)
            res.append(node.val)
            dfs(node.right)

        dfs(root)
        return res[k- 1]

        
      
