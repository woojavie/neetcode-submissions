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
            cur += "("
            open += 1
            dfs(open, close, cur)

            cur = cur[:-1]
            open -= 1
            cur += ")"
            close += 1
            dfs(open, close, cur)
        dfs(0, 0, "")
        return res