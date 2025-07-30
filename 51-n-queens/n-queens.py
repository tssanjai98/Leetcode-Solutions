class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def dfs(board, row, col):
            if row not in range(n) or col not in range(n) or board[row][col] == 'X':    return
            board[row][col], marked= 'Q', [(row, col)]
            
            if row == n-1:
                boardCopy = [row[:] for row in board]
                board[row][col] = '.'
                for r in range(n):
                    for c in range(n):
                        if boardCopy[r][c] == 'X':      boardCopy[r][c] = '.'
                res.append(["".join(row) for row in boardCopy])
                return
            
            directions = [[0,-1], [-1,-1], [-1,0], [-1,1], [0,1], [1,1], [1,0], [1,-1]]
            for r_dir, c_dir in directions:
                rDiag, cDiag = row + r_dir, col + c_dir
                while rDiag in range(n) and cDiag in range(n):
                    if board[rDiag][cDiag] == '.':
                        board[rDiag][cDiag] = 'X'
                        marked.append((rDiag, cDiag))
                    rDiag, cDiag = rDiag+r_dir, cDiag+c_dir
            for col in range(n):    dfs(board, row+1, col)
            for r, c in marked:     board[r][c] = '.'
            
            
        for col in range(n):    dfs([["." for i in range(n)] for i in range(n)], 0, col)
        return res