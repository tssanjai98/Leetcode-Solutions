class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ms = nums[0]
        cs = 0

        for i in nums:
            if cs < 0:
                cs = 0
            cs += i
            ms = max(ms, cs)

        return ms