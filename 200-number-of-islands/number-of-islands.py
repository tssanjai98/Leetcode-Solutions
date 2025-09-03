class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands = 0
        visited = set()
        

        def bfs(r,c):
            q = collections.deque()
            q.append((r,c))
            visited.add((r,c))
            directions = [[1,0],[-1,0],[0,1],[0,-1]]
            while q:
                r,c = q.pop()
                for dr,dc in directions:
                    row, col = r+dr, c+dc
                    if (row >= 0 and col >= 0 and row < rows and col < cols and grid[row][col] == '1' and (row,col) not in visited):
                        visited.add((row,col))
                        q.append((row,col))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r,c) not in visited:
                    bfs(r,c)
                    islands += 1

        return islands