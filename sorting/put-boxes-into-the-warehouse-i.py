class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort()
        n = len(warehouse)
        output = 0
        for i in range(1, n):
            warehouse[i] = min(warehouse[i], warehouse[i-1])
        for j in range(n-1, -1, -1):
            if output < len(boxes) and boxes[output] <= warehouse[j]:
                output += 1
        return output