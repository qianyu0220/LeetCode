class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort()
        for i in range(1, len(warehouse)):
            warehouse[i] = min(warehouse[i], warehouse[i-1])
        i_1 = 0
        for j in range(len(warehouse)-1, -1, -1):
            if boxes[i_1] <= warehouse[j] and i_1 < len(boxes):
                i_1 += 1
        i_2 = 0
        for j in range(len(warehouse)):
            if boxes[i_2] <= warehouse[j] and i_2 < len(boxes):
                i_2 += 1
        return max(i_1, i_2)