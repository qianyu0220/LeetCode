class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([s for s, e in intervals])
        ends = sorted([e for s, e in intervals])
        i = j = 0
        rooms = max_room = 0
        while i < len(starts):
            if starts[i] < ends[j]:
                rooms += 1
                max_room = max(rooms, max_room)
                i += 1
            else:
                rooms -= 1
                j += 1
        return max_room