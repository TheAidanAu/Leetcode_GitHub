class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort input intervals and iterate
        # Look at prevEnd, check if it overlaps the current start
        # if it doesn't, advance the prevEnd
        # else increment the remove count
        # and keep intervals with a sooner end time
        # Greedy approach: take classes which ends as early as possible so that you can take as many classes as possible
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(end, prevEnd)

        return res

# Time: O(NlogN) + o(n) = O(NlogN)
# Space: O(1)