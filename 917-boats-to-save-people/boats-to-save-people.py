class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        l = 0 
        r = len(people) - 1
        res = 0

        while l <= r:

            if l < r and people[r] + people[l] <= limit:
                res += 1
                r -= 1
                l += 1
            
            else:
                r -= 1
                res += 1
                
        return res



        