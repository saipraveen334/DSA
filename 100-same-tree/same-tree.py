# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #BFS 
        q1 = deque([q])
        q2 = deque([p])

        while q1 and q2:

            for _ in range(len(q1)):

                nodeq = q1.popleft()
                nodep = q2.popleft()

                if nodeq is None and nodep is None:
                    continue

                if nodeq is None or nodep is None or nodeq.val != nodep.val:
                    return False

                q1.append(nodeq.left)
                q2.append(nodep.left)
                q1.append(nodeq.right)
                q2.append(nodep.right)
        return True 
                




        #DFS 
        if not p and not q:
            return True 
        
        if p and q and p.val == q.val:
            return self.isSameTree(p.left , q.left) and self.isSameTree(p.right , q.right)
        else:
            return False
        