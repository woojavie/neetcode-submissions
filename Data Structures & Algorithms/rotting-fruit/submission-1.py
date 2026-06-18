class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = deque()
        visit = set()
        minute = 0
        def addOrange(r, c):
            if (min(r, c) < 0 or r == rows or c == cols or
                (r, c) in visit or grid[r][c] != 1):
                return
            visit.add((r, c))
            q.append((r, c))
            grid[r][c] = 2

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visit.add((r, c))

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                addOrange(r + 1, c)
                addOrange(r - 1, c)
                addOrange(r, c + 1)
                addOrange(r, c - 1)
            if q:
                minute += 1
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    return -1
        return minute
