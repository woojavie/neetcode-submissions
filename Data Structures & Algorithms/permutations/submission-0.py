class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        chosen = [False for num in nums]
        
        def dfs(cur):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            for i in range(len(chosen)):
                if chosen[i] == False:
                    cur.append(nums[i])
                    chosen[i] = True
                    dfs(cur)
                
                    cur.pop()
                    chosen[i] = False

        dfs([])
        return res 
