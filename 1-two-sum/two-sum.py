class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSet = {}
        for i in range(len(nums)):
            if nums[i] in hashSet:
                return [i, hashSet[nums[i]]]
            diff = target - nums[i]
            hashSet[diff] = i
        return [-1, -1]

            