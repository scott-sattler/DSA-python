"""
iff meetings are ordered:
    end of current meeting must be <= start of next meeting

sorting requires O(n * log n)

"""


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))
        length = len(intervals)
        for i in range(1, length):
            if intervals[i - 1][1] > intervals[i][0]:
                return False
        return True
