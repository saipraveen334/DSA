# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        res = 0

        def dfs(root):

            if not root:
                return ( 0 , 0 ) # num of Nodes , totalsum

            nonlocal res 

            leftN , leftSum = dfs(root.left)
            rightN , rightSum = dfs(root.right)

            n = leftN + rightN + 1
            totalSum = leftSum + rightSum + root.val

            if (totalSum // n == root.val):
                res += 1
            
            return(n , totalSum)
         
        dfs(root)
        return res
        