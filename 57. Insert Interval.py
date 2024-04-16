class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # iternate the arrays, check if newInterval is before or after a current interval
        # if they overlap, merge them (taking the min and max of start and end resp.)
        # Finally, we add the merged or non-overlapping newInterval to res.

        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                # because everything else after newInterval are not overlapped 
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                # just append the current interval without the new interval 
                # because the newInterval may or may not overlap 
                res.append(intervals[i])
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        # Finally, we add the merged or non-overlapping newInterval to res.
        res.append(newInterval)
        return res

# Time: O(N)
# Space: O(N)   