class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        return sorted([[a**2 + b**2, a * b] for a, b in dimensions], key=lambda x: (x[0], x[1]))[-1][1]