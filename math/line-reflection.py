class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        points_set = set()
        minX = float("inf")
        maxX = -float("inf")
        for p in points:
            points_set.add((p[0], p[1]))
            minX = min(minX, p[0])
            maxX = max(maxX, p[0])
        centerX = (minX + maxX) / 2
        for p in points:
            x, y = p[0], p[1]
            if (2 * centerX - x, y) not in points_set:
                return False
        return True