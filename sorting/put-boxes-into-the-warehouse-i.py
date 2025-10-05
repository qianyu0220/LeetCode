class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        # boxes.sort()
        # for i in range(1, len(warehouse)):
        #     warehouse[i] = min(warehouse[i], warehoue[i - 1])
        # i = 0
        # for j in reversed(range(len(warehouse))):
        #     if i < len(boxes) and boxes[i] <= warehouse[j]:
        #         i += 1
        # return i
        boxes.sort()
        for i in range(1, len(warehouse)):
            warehouse[i] = min(warehouse[i-1], warehouse[i])
        i = 0
        for j in range(len(warehouse)-1, -1, -1):
            if i < len(boxes) and boxes[i] <= warehouse[j]:
                i += 1
        return i