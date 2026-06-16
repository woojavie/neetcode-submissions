class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        area = 0
        rows, cols = len(grid), len(grid[0])
        visit = set()

        def bfs(r, c, area):
            q = deque()
            q.append((r, c))
            visit.add((r, c))

            while q:
                row, col = q.popleft()
                directions = [[0,1], [0,-1], [1,0], [-1,0]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if ((r in range(rows)) and 
                        (c in range(cols)) and 
                        (grid[r][c] == 1) and 
                        ((r, c) not in visit)):
                        area += 1
                        visit.add((r, c))
                        q.append((r, c))
            return area
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visit:
                    area = max(area, bfs(r, c, 1))

        return area
                