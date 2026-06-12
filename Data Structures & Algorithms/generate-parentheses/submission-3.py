class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(open, closed, cur):
            if open > n or closed > n or closed > open:
                return
            if len(cur) == (2 * n):
                res.append(cur)
                return

            dfs(open + 1, closed, cur + "(")
            dfs(open, closed + 1, cur + ")")
        dfs(0,0,"")
        return res