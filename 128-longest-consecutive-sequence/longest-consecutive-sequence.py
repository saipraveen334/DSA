class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #REMOVE DUPLICATES AND FIND STARTING POINT CONSECUTIVE ELEMENTS TO AVOID TIME COMPLEXITY 

        nums1 = set(nums)
        maxStreak = 0

        for n in nums1:

            if (n + 1) not in nums1:

                length = 1

                while (n - length) in nums1:
                    length += 1

                maxStreak = max(maxStreak , length)

        return maxStreak 
        