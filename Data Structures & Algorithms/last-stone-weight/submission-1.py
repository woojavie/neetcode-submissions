class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for i in range(len(stones)):
            heapq.heappush(maxHeap, -stones[i])
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            x = heapq.heappop(maxHeap)
            y = heapq.heappop(maxHeap)
            if x != y:
                heapq.heappush(maxHeap, -((y) - (x)))
        if maxHeap:
            return -maxHeap[0]
        return 0

