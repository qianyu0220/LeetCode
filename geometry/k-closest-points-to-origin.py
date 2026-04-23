class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        output = []
        for i in points:
            heapq.heappush(heap, (i[0]**2 + i[1]**2, i))
        for i in range(k):
            output.append(heapq.heappop(heap)[1])
        return output
