class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # draw a number line to solve intervals questions
        # sort each interval by start time to detect overlaps,
        # interate the sorted list and merge overlapped intervals
        # add the first interval in the res array to avoid edge case
        # check the next start time and the prev end time
        # update the prev end time with the MAX of both end times in case the prev interval is longer
        intervals.sort(key=lambda i: i[0])
        res = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]
            if start <= lastEnd:
                res[-1][1] = max(lastEnd, end)
            else:
                res.append([start, end])
        return res

# time: O(nlogn) + O(N) = O(NlogN)
# Space: O(N)





