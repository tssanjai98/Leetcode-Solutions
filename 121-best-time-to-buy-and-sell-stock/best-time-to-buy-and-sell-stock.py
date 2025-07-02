class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minPrice = float('inf')
        maxProf = 0
        for i in range(len(prices)):
            minPrice = min(prices[i], minPrice)
            diff = prices[i] - minPrice
            maxProf = max(diff, maxProf)
        return maxProf
