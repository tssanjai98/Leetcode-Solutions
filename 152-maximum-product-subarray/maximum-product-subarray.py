class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        cma, cmi = 1,1

        for n in nums:
            if n == 0:
                cma, cmi = 1,1
                continue
            tmp = cma * n
            cma = max(n*cma, n*cmi, n)
            cmi = min(tmp, n*cmi, n)
            res = max(res, cma)
        return res