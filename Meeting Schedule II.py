"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # max number of overlapped meetings at any given point in time
        # sort the input array
        # we care about the points in time where we start/end a meeting,
        # we already are given those,
        # just separate start/end and traverse counting num of meetings going at these points in time; for each meeting check
        # if a prev meeting has finished before curr started, using min heap;
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])
        res, count = 0, 0
        s, e = 0, 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1
            res = max(res, count)

        return res
# Time: O(NlogN) for sorting
# Space: O(N) 