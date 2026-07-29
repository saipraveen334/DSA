class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(perm, existing):
            if len(perm) == n:
                res.append(perm[:])
                return
            for i in nums:
                if i not in existing:
                    perm.append(i)
                    existing.add(i)
                    dfs(perm, existing)
                    perm.pop()      
                    existing.discard(i)

        dfs([], set())
        return res