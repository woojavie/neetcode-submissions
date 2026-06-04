class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i in range(len(points)):
            distance = math.sqrt((points[i][0] ** 2) + (points[i][1] ** 2))
            heapq.heappush(heap, [-distance, tuple(points[i])])
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for key,value in heap:
            res.append(value)
        return res