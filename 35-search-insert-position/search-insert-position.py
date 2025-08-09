class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        count = 0
        y_ans = 0
        n_ans = 0
        p = 0
        l = 0
        while count < len(nums):
            if target == nums[count]:
                y_ans = count
                l += 1
                break
            count += 1
        if l != 1:
            for count in range(0,len(nums)):
                if nums[count] > target:
                    n_ans = count
                    p = 1
                    break
            if p == 1:
                return n_ans
            else:
                return len(nums)
        else:
            return y_ans