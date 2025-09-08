class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(n):
            diff = n-i
            if ('0' not in str(diff)) and ('0' not in str(i)):
                return [i,diff]
                