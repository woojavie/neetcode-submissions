class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(open, close, cur):
            if len(cur) == (2 * n) and open == close:
                res.append(cur)
                return
            
            if open > n or close > n:
                return

            if close > open:
                return

            dfs(open + 1, close, cur + "(")
            dfs(open, close + 1, cur + ")")
        dfs(0, 0, "")
        return res