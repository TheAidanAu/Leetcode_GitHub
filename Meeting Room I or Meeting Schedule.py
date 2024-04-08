"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort intervals by start time in a lambda function,
        # if second interval doesn’t overlap with first,
        # then third def wont overlap with first;
        intervals.sort(key = lambda i:i.start)

        for i in range(1,len(intervals)):
            i1 = intervals[i-1]
            i2 = intervals[i]
            if (i2.start < i1.end):
                return False
        return True
# time: o(NlogN) + O(N) = o(NlogN) because of sorting

