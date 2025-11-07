class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        for i in points:
            heapq.heappush(distance, (i[0]**2 + i[1]**2, i))
        k_points = []
        for i in range(k):
            k_points.append(heapq.heappop(distance)[1])
        return k_points