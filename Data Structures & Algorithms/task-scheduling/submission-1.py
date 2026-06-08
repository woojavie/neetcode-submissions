class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {} # tasks : count
        for t in tasks:
            count[t] = 1 + count.get(t, 0)
        time = 0
        maxHeap = [-num for num in count.values()]
        heapq.heapify(maxHeap)
        q = deque()
        while maxHeap or q:
            time += 1
            if maxHeap:
                task = heapq.heappop(maxHeap)
                task += 1
                if task:
                    q.append([task, n + time])
            if q and q[0][-1] == time:
                nextTask = q.popleft()
                
                heapq.heappush(maxHeap, nextTask[0])
        return time

