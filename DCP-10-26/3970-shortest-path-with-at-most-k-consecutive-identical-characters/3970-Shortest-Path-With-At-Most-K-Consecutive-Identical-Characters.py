import heapq
from typing import List

class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))

        K = k + 1
        INF = 10**18
        dist = [INF] * (n * K)       # index: node * K + run
        dist[1] = 0                  # node 0, run 1
        pq = [(0, 0, 1)]             # (cost, node, run)

        while pq:
            d, u, run = heapq.heappop(pq)
            if d > dist[u * K + run]:
                continue
            if u == n - 1:
                return d
            lu = labels[u]
            for v, w in adj[u]:
                nrun = run + 1 if labels[v] == lu else 1
                if nrun > k:
                    continue
                nd = d + w
                idx = v * K + nrun
                if nd < dist[idx]:
                    dist[idx] = nd
                    heapq.heappush(pq, (nd, v, nrun))

        return -1