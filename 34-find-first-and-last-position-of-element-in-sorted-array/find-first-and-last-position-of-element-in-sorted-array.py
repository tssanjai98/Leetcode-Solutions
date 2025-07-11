class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        right = len(nums) - 1 if len(nums) > 0 else 0
        left = 0
        first, last = -1, -1

        while left <= len(nums) - 1:
            if nums[left] == target:
                first = left
                break
            left+=1
        
        while right >= 0:
            if len(nums) > 0 and nums[right] == target:
                last = right
                break
            right -= 1

        return [first, last]

