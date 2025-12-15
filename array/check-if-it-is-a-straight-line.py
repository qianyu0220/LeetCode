class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        n = len(coordinates)
        diff = (coordinates[1][1] - coordinates[0][1]) / (coordinates[1][0] - coordinates[0][0])

        for i in range(1, n):
            if (coordinates[i][1] - coordinates[i-1][1]) / (coordinates[i][0] - coordinates[i-1][0]) != diff:
                return False
        return True
