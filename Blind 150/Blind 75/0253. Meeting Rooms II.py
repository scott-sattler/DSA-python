"""
end_1 <= start_2

sort in O(n * log n)

keep sorted list of completion times
track largest size...

heapq

"""
import heapq


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        max_rooms = 1
        booked_rooms = []

        intervals = sorted(intervals, key=lambda x: (x[0], x[1]))

        for interval in intervals:
            # start_t is the current time
            # clear all rooms that have since
            # had their meetings end
            start_t = interval[0]
            while booked_rooms and start_t >= booked_rooms[0]:
                heapq.heappop(booked_rooms)

            heapq.heappush(booked_rooms, interval[1])
            max_rooms = max(len(booked_rooms), max_rooms)

        return max_rooms
