class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = 0


        while l <= r:

            m = (l + r) // 2

            total = 0 
            reqdays = 1

            for w in weights:
                if total + w > m:
                    reqdays += 1
                    total = 0

                total += w

            
            if reqdays <= days:
                res = m
                r = m - 1 
            else:
                l = m + 1
        return res
        