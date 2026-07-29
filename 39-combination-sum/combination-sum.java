class Solution
{
    public List<List<Integer>> combinationSum(int[] candidates, int target)
    {
        List<List<Integer>> res = new ArrayList<>();
        dfs(candidates, target, 0, new ArrayList<>(), 0, res);
        return res;
    }

    private void dfs(int[] candidates, int target, int i, List<Integer> cur, int total, List<List<Integer>> res)
    {
        if (total == target)
        {
            res.add(new ArrayList<>(cur));
            return;
        }

        if (i >= candidates.length || total > target)
        {
            return;
        }

        cur.add(candidates[i]);
        dfs(candidates, target, i, cur, total + candidates[i], res);

        cur.remove(cur.size() - 1);
        dfs(candidates, target, i + 1, cur, total, res);
    }
}