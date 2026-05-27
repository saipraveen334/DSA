class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0 
        r = len(nums) - 1

        while l <= r:

            mid = l + ( r - l ) // 2

            if target == nums[mid]:
                return True 

            # LEFT PORTION
            if nums[mid] > nums[l]:

                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            
            #RIGHT PORTION 

            elif nums[mid] < nums[l]:

                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1 
            else:
                l += 1
        return False 


                 
                

