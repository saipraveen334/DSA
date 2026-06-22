# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # ITERATIVE APPROACH 1
        stack = [root]
        visit = [False]
        res = []

        while stack:
            cur, v = stack.pop(), visit.pop()
            if cur:
                if v:
                    res.append(cur.val)
                else:
                    stack.append(cur)
                    visit.append(True)
                    stack.append(cur.right)
                    visit.append(False)
                    stack.append(cur.left)
                    visit.append(False)

        return res
        
        # ITERATIVE APPROACH 2
        cur = root 
        stack = []
        res = []

        while cur or stack:
            if cur:
                res.append(cur.val)
                stack.append(cur.left)
                cur = cur.right
            else:
                cur = stack.pop()
            
        return res[::-1]


        #RECURSIVE APPROACH 

        res = []

        def postorder(root):

            if not root:
                return 

            postorder(root.left)
            postorder(root.right)
            res.append(root.val)

        postorder(root)
        return res 
        