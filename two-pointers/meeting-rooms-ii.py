class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([s for s, e in intervals])
        ends = sorted([e for s, e in intervals])
        rooms = max_rooms = 0
        i = j = 0
        while i<len(intervals) and j<len(intervals):
            if starts[i] < ends[j]:
                rooms += 1
                max_rooms = max(max_rooms, rooms)
                i += 1
            else:
                rooms -= 1
                j += 1
        return rooms