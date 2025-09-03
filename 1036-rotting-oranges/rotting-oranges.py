class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = collections.deque()
        mins = 0
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if (grid[r][c] == 2 and (r,c) not in visited):
                    q.append((r,c))
                    visited.add((r,c))
                if (grid[r][c] == 1):
                    fresh += 1
        # if fresh == 0:
        #     return 0

        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                directions = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in directions:
                    nr, nc = row+dr, col+dc
                    if (nr<0 or
                        nc<0 or
                        nr == rows or
                        nc == cols or
                        grid[nr][nc] == 0 or
                        grid[nr][nc] == 2 or
                        (nr,nc) in visited):
                        continue
                    q.append((nr,nc))
                    visited.add((nr,nc))
                    fresh-=1
            mins+=1

        return max(0,mins - 1)  if fresh == 0 else -1