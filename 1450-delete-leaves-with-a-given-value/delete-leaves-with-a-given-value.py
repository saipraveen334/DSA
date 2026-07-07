# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        # POST ORDER TRAVERSAL REMOVAL METHOD 
        stack = [root]
        visit = set()
        parents = { root : None }

        while stack:
            node = stack.pop()

            if not node.right and not node.left and target == node.val:
                p = parents[node]

                if not p:
                    return None

                # PART EXACTLY WHERE THE NODE GETS UNLINKED (DELETED) 

                if p and p.left == node:
                    p.left = None 
                if p and p.right == node:
                    p.right = None

            elif node not in visit:
                visit.add(node)
                stack.append(node)

                if node.left:
                    stack.append(node.left)
                    parents[node.left] = node 
                if node.right:
                    stack.append(node.right)
                    parents[node.right] = node
        return root

                
                



        # RECURSIVE APPROACH 

        if not root:
            return None 
        
        root.left = self.removeLeafNodes(root.left , target)
        root.right = self.removeLeafNodes(root.right , target)


        if not root.left and not root.right and target == root.val:
            return None
        
        return root
        
        