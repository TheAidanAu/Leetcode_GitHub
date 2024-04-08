class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort input intervals and iterate
        # Look at prevEnd, check if it overlaps the current start
        # if it doesn't, advance the prevEnd
        # else increment the remove count and also update the prevEnd with a sooner end time
        # Greedy approach: take classes which ends as early as possible so that you can take as many classes as possible
        # overlapped cases:
        # ---               --------            ----------
        #.       -----           ------             ----
        intervals.sort()
        prevEnd = intervals[0][1]
        res = 0

        for start, end in intervals[1:]:
            if start < prevEnd:
                res += 1
                prevEnd = min(end, prevEnd)
            else:
                prevEnd = end
        return res

# Time: O(NlogN) + o(n) = O(NlogN)
# Space: O(1)
