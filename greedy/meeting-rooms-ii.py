class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted(s for s, _ in intervals)
        ends = sorted(e for _,e in intervals)
        i = j = 0
        rooms = 0
        max_rooms = 0
        while i < len(starts):
            if starts[i] < ends[j]:
                rooms += 1
                max_rooms = max(rooms, max_rooms)
                i += 1
            else:
                rooms -= 1
                j += 1
        return max_rooms