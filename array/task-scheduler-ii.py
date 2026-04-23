class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        last = {}
        day = 0
        for task in tasks:
            day += 1
            if task in last and day <= last[task] + space:
                day = last[task] + space + 1
            last[task] = day
        return day