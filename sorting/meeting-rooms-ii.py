class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([s for s, e in intervals])
        ends = sorted([e for s, e in intervals])
        i = j = 0
        room = max_room = 0
        while i < len(starts):
            if starts[i] < ends[j]:
                room += 1
                max_room = max(room, room)
                i += 1
            else:
                room -= 1
                j += 1
        return max_room
