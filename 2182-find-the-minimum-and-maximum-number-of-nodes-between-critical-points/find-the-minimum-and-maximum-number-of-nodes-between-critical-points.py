# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        # get length
        length = 0 
        curr = head 

        while curr:
            length += 1
            curr = curr.next 
        
        if length < 3:
            return [-1 , -1]
        
        prev = head
        cur = head.next 
        criticalPoint = []

        for i in range(length - 2):
            if prev.val > cur.val < cur.next.val:
                criticalPoint.append(i + 1)
            if prev.val < cur.val > cur.next.val:
                criticalPoint.append(i + 1)
            
            cur = cur.next
            prev = prev.next 

        # what if there is only 1 critical point 
        if len(criticalPoint) < 2:
            return [-1 , -1]
        
        # for calculatind mindis 
        mindis = length 
        for i in range(len(criticalPoint) - 1):
            mindis = min((criticalPoint[i + 1] - criticalPoint[i]), mindis)
        
        maxdis = criticalPoint[-1] - criticalPoint[0]

        return [mindis , maxdis]
            
        

        
            



        