class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        x=0
        if n>0:
            x=(math.log(n,2))//2
        return 4**x==n and n>0