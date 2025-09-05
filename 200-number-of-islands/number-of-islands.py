class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # 1,1,1,0
        # 1,1,1,0
        # 1,0,0,0
        # 0,0,1,0
        # 1,1,0,0

        # set to track if the island is visited (m,n)
        # dfs(m,n) in all directions

        m, n = len(grid), len(grid[0])

        visited = set()

        number_of_islands = 0

        def dfs(i,j):
            if i < 0 or j < 0 or i == m or j == n or grid[i][j] == "0" or (i,j) in visited:
                return
            else:
                visited.add((i,j))
                dfs(i+1,j)
                dfs(i-1,j)
                dfs(i,j+1)
                dfs(i,j-1)


        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and (i,j) not in visited:
                    number_of_islands+=1
                    dfs(i,j)

        return number_of_islands



