class Solution(object):
    def maxFrequency(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        freq,first,last = [0]*51,[-1]*51,[-1]*51
        res = 0

        ps = [0]
        for a in nums: ps.append(ps[-1] + (1 if a ==k else 0))

        for i in range(len(nums)): 
            v = nums[i]
            if v == k: continue
            freq[v] += 1
            if first[v] == -1: first[v] = i
            last[v] = i

            numberOfKs = ps[last[v]+1] - ps[first[v]+1]
            net = freq[v] - numberOfKs
            if net <= 0: 
                first[v] = i
                freq[v] = 1
            res = max(res,net)

        return res + ps[-1]