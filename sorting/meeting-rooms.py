class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        n = len(intervals)
        intervals.sort(key=lambda x:x[0])
        for i in range(n):
            if i > 0 and intervals[i][0] < intervals[i-1][1]:
                return False
        return True