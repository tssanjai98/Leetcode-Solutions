class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 1  3
        #   2  6
        #        8    10
        #                     15  18

        # are the arrays sorted? No -> sort
        # sort
        # check the start value of interval to the most recent end value
        # if less or equal then we will merge them

        intervals.sort(key = lambda i: i[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            recentEnd = res[-1][1]

            if start <= recentEnd:
                res[-1][1] = max(recentEnd, end)

            else:
                res.append([start,end])

        return res
