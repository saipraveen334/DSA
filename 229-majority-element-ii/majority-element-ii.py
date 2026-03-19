class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = defaultdict(int)

        for n in nums:

            count[n] += 1

            if len(count) <= 2:
                continue

            new_count = defaultdict(int)

            for n , val in count.items():

                if val > 1:
                    new_count[n] = val - 1
            count = new_count
        res = []

        for num in count:
            if nums.count(num) > len(nums) //3:
                res.append(num)
        return res


        