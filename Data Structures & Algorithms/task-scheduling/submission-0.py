class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxHeap = []
        count = {}
        q = deque()
        time = 0
        for i in range(len(tasks)):
            count[tasks[i]] = 1 + count.get(tasks[i], 0)
        for k in count:
            maxHeap.append(-count[k])
        heapq.heapify(maxHeap)

        while maxHeap or q:
            time += 1
            if maxHeap:
                task = heapq.heappop(maxHeap)
                task += 1
                if task:
                    q.append([task, n + time])
            if q and q[0][-1] == time:
                task2 = q.popleft()
                heapq.heappush(maxHeap, task2[0])
        return time