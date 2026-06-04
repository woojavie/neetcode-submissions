class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distMap = {}
        for i in range(len(points)):
            distMap[tuple(points[i])] = math.sqrt((points[i][0] ** 2) + (points[i][1] ** 2))

        heap = [(value, key) for key, value in distMap.items()]

        heapq.heapify(heap)
        res = []
        for point in range(k):
            res.append(heapq.heappop(heap)[1])
        return res