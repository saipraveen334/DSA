# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # DFS + DFS APPROACH 
        if not subRoot:
            return True 
        if not root:
            return False 
        
        if self.sameTree(root , subRoot):
            return True 
        
        return self.isSubtree(root.left , subRoot) or self.isSubtree(root.right , subRoot)
    
    def sameTree( self , p : Optional[TreeNode] , q: Optional[TreeNode]):
        if not p and not q:
            return True 
        if p and q and p.val == q.val:
            return self.sameTree(p.right , q.right) and self.sameTree(p.left , q.left)
        else:
            return False 

        q = deque([root])

        while q:
            for _ in range(len(q)):
                node = q.popleft()

                if node.val == subRoot.val:
                    if self.sametree(node , subRoot):
                        return True 
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return False 


    

    def sametree(self , p: Optional[TreeNode] , q:Optional[TreeNode]):
        if not p and not q:
            return True 
        
        if p and q and p.val == q.val:
            return self.sametree(p.left , q.left) and self.sametree(p.right,q.right)
        else:
            return False 

        