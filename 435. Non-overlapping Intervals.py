class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort input intervals and iterate
        # prevEnd is initialized as the first sorted interval's end time
        # interate through the sorted array
        # best case is there's no overlap and prevEnd would be udpated with the current end time only
        # if there's an overlap, update with an earlier end time
        # increment the times to removal by 1

        # Greedy approach: take classes which ends as early as possible so that you can take as many classes as possible
        # overlapped cases:
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
