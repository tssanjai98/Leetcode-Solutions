class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}
        for i in range(len(nums)):
            if nums[i] in hashset.keys():
                return [i, hashset[nums[i]]]
            diff = target - nums[i]
            hashset[diff] = i

        return [-1,-1]
