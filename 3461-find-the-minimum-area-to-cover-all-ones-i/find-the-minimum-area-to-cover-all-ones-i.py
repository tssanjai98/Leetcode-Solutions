class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        minx=-1
        miny=-1
        maxx=-1
        maxy=-1
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                    if miny == -1:
                        miny = y
                        maxy = y
                    if minx == -1:
                        minx = x
                        maxx = x
                    if maxx < x:
                        maxx=x
                    if maxy < y:
                        maxy = y
                    if y < miny:
                        miny = y
        return (maxy-miny+1) * (maxx-minx+1)