class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s = set()
            for j in range(9):
                val = board[i][j]
                if val in s:
                    return False
                elif val != ".":
                    s.add(val)

        for i in range(9):
            s = set()
            for j in range(9):
                val = board[j][i]
                if val in s:
                    return False
                elif val != ".":
                    s.add(val)

        starts = [
            (0,0), (0,3), (0,6),
            (3,0), (3,3), (3,6),
            (6,0), (6,3), (6,6),
        ]

        for i, j in starts:
            s = set()
            for row in range(i,i+3):
                for col in range(j,j+3):
                    val = board[row][col]
                    if val in s:
                        return False
                    elif val != ".":
                        s.add(val)

        return True