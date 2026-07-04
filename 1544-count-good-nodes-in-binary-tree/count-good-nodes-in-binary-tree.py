# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        #BFS 

        q = deque()
        q.append((root , -float("inf")))
        res = 0

        while q:
            for _ in range(len(q)):
                node , maxVal = q.popleft()

                if node.val >= maxVal:
                    res += 1

                if node.left:
                    q.append((node.left , max(maxVal , node.val)))
                if node.right:
                    q.append((node.right , max(maxVal , node.val)))
        return res



        #DFS 
        res = 0

        def dfs(node , maxVal):

            nonlocal res

            if not node:
                return 0

            res += 1 if node.val >= maxVal else 0 

            maxVal = max(maxVal , node.val)

            dfs(node.left , maxVal)
            dfs(node.right , maxVal)

            return res

        return dfs(root , root.val)


                
            
        