import heapq
from typing import List

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        free = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(free)
        busy = []  # (free_time, weight, index)
        res = []
        t = 0

        for j, dur in enumerate(tasks):
            t = max(t, j)  # task j is not available before second j

            # release every server that has finished by time t
            while busy and busy[0][0] <= t:
                ft, w, i = heapq.heappop(busy)
                heapq.heappush(free, (w, i))

            # no free server: jump ahead to the earliest completion
            if not free:
                t = busy[0][0]
                while busy and busy[0][0] <= t:
                    ft, w, i = heapq.heappop(busy)
                    heapq.heappush(free, (w, i))

            w, i = heapq.heappop(free)
            res.append(i)
            heapq.heappush(busy, (t + dur, w, i))

        return res