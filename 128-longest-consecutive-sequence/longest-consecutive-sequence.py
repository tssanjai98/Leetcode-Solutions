class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longest = 0
        for n in numsSet:
            if (n - 1) not in numsSet:
                nextNum = n + 1
                length = 1
                while nextNum in numsSet:
                    length += 1
                    nextNum +=1
                longest = max(length, longest)
        return longest


