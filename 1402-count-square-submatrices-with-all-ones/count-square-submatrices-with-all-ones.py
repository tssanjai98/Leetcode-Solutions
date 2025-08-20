class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        cumsum, prev_row = sum(matrix[0]), matrix[0]
        if m == 1:
            return cumsum

        for i in range(1, m):
            curr_row = []
            for j in range(n):
                if j == 0:
                    curr_row.append(matrix[i][0])
                else:
                    max_square = 0 if matrix[i][j] == 0 else 1 + min(curr_row[j-1], prev_row[j-1], prev_row[j])
                    curr_row.append(max_square)
            cumsum += sum(curr_row)
            prev_row = curr_row

        return cumsum