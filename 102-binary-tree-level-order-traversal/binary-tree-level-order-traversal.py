# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # DFS 

        res = []

        def dfs(node, level):
            if not node:
                return None
            
            if len(res) == level:
                res.append([])
            
            res[level].append(node.val)

            dfs(node.left , level + 1)
            dfs(node.right , level + 1)

        dfs(root , 0)
        return res



        #BFS 

        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            l = []
            for _ in range(len(q)):
                node = q.popleft()
                l.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.append(l)
        return res
                


        