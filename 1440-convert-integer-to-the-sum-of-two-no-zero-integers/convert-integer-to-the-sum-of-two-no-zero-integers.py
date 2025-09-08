class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        valid_ints = []
        for i in range(n):
            if '0' not in str(i):
                valid_ints.append(i)

        for i in valid_ints:
            diff = n-i
            if diff in valid_ints:
                return [i,diff]