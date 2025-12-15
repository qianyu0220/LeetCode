class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        x = [ax1, ax2, bx1, bx2]
        y = [ay1, ay2, by1, by2]
        x.sort()
        y.sort()
        area1 = (ax1 - ax2) * (ay1 - ay2)
        area2 = (bx1 - bx2) * (by1 - by2)

        return (area1 + area2) - (x[1] - x[2]) * (y[1] - y[2])