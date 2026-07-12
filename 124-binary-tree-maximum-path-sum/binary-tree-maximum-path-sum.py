# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # O(N) solution 
        res = root.val

        def dfs(root):
            if not root:
                return 0 

            nonlocal res 

            left= dfs(root.left)
            right = dfs(root.right)

            leftMax = max(left , 0)
            rightMax = max(right , 0)
        

            res = max(res , root.val + leftMax + rightMax)

            return root.val + max(leftMax , rightMax) #SENDIND THE VALUE YOU GET MOST OF IT FROM 

        dfs(root)
        return res 
        
        res = float("-inf")

        def gettingMax(root):

            if not root:
                return 0 
            
            #IF NO NODES PRESENT THEN RETURN 0 CAUSE WE NEED MAX(SUM)

            left = gettingMax(root.left)
            right = gettingMax(root.right)

            path = root.val + max(left , right)

            return max(path , 0) # HANDLING NEGATIVE VALUES 


        # GET MAX FORM INDIVIDUAL NODE 

        def dfs(root):
            if not root:
                return  
                # WE ARE RETURING NOTHING BECAUSE WE ARE NOT GETTING VALUES FROM THIS FUCNTION ,THIS FUMCTION IS JUST FOR INDIVIDUAL NODE CALCULATION
            
            nonlocal res
            # NOW GETTING THE MAX VALUES FROM LEFT AND RIGHT FROM OTHER FUNCTION 

            left = gettingMax(root.left)
            rigth = gettingMax(root.right)

            # CALCULATE RES 
            # INCLUDING THE ROOT VALUE CAUSE THE ROOT IS NECCESSARY FOR PATH 

            res = max(res , root.val + left + rigth)

            #FOR EACH NODE WE NEED MAX

            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return res 

        



            
            

            
                 
        