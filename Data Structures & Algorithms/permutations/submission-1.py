class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        chosen = [False] * len(nums)

        def dfs(cur, chosen):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            for i in range(len(chosen)):
                if not chosen[i]:
                    cur.append(nums[i])
                    chosen[i] = True
                    dfs(cur, chosen)

                    cur.pop()
                    chosen[i] = False
        dfs([], chosen)
        return res
