class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:

        # get length
        length = 0
        curr = head

        while curr:
            length += 1
            curr = curr.next

        if length < 3:
            return [-1, -1]

        prev = head
        cur = head.next
        criticalPoint = []

        for i in range(length - 2):

            if (prev.val > cur.val < cur.next.val) or \
               (prev.val < cur.val > cur.next.val):
                criticalPoint.append(i + 1)

            cur = cur.next
            prev = prev.next

        # fewer than 2 critical points
        if len(criticalPoint) < 2:
            return [-1, -1]

        # minimum distance
        mindis = length

        for i in range(len(criticalPoint) - 1):
            mindis = min(
                mindis,
                criticalPoint[i + 1] - criticalPoint[i]
            )

        # maximum distance
        maxdis = criticalPoint[-1] - criticalPoint[0]

        return [mindis, maxdis]