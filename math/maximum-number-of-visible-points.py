class Solution:
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        x0, y0 = location
        same = 0
        angles = []
        for x, y in points:
            dx = x - x0
            dy = y - y0
            if dx == 0 and dy == 0:
                same += 1
            else:
                angles.append(math.degrees(math.atan2(dy, dx)))
        angles.sort()
        n = len(angles)
        angles += [a+360 for a in angles]

        max_count = 0
        j = 0
        for i in range(n):
            while j < len(angles) and angles[j] - angles[i] <= angle:
                j += 1
            max_count = max(max_count, j - i)
        return max_count + same
