class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()
        nums_sorted = sorted(nums)
        for i in range(len(nums)):
            j = i+1
            k = len(nums_sorted) - 1 
            while(j<k):
                tsum = nums_sorted[i] + nums_sorted[j] + nums_sorted[k]
                if(tsum == 0):
                    res.add(tuple([nums_sorted[i] , nums_sorted[j] , nums_sorted[k]]))
                    j+=1
                    k-=1
                    while(j < k and nums_sorted[k] == nums_sorted[k+1]):
                        k-=1
                    while(j < k and nums_sorted[j] == nums_sorted[j-1]):
                        j+=1
                elif(tsum > 0):
                    k -= 1
                    
                elif(tsum < 0):
                    j+=1

        return [list(i) for i in res]
            