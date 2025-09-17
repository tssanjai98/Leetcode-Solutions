class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lmul = 1
        rmul = 1
        n = len(nums)
        larr = [0] * n
        rarr = [0] * n

        for i in range(n):
            j = -i - 1
            larr[i] = lmul
            rarr[j] = rmul
            lmul *= nums[i]
            rmul *= nums[j]

        res = []
        for i in range(n):
            res.append(larr[i] * rarr[i])

        return res