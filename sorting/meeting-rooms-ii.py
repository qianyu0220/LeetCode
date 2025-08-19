class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        starts = sorted([s for s, _ in intervals])
        ends = sorted([e for _, e in intervals])
        i = j = 0
        rooms = max_room = 0
        while i < len(starts):
            if starts[i] < ends[j]:
                rooms += 1
                max_room = max(max_room, rooms)
                i += 1
            else:
                rooms -= 1
                j += 1
        return max_room
            
