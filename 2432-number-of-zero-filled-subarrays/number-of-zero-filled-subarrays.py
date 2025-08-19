class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        sol = 0
        con_z = 0
        for n in nums:
            if n and con_z:
                sol += con_z*(con_z+1)//2
                con_z = 0
            elif not n:
                con_z += 1
        sol += con_z*(con_z+1)//2
        return sol