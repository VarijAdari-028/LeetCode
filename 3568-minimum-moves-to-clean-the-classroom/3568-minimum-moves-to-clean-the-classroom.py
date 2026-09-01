import heapq

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litter = []
        start = None
        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter.append((i, j))

        L = len(litter)
        if L == 0:
            return 0

        litter_idx = {pos: k for k, pos in enumerate(litter)}
        full_mask = (1 << L) - 1

        start_mask = 0
        if start in litter_idx:
            start_mask |= (1 << litter_idx[start])
        best_energy = [[[-1] * (1 << L) for _ in range(n)] for _ in range(m)]
        best_energy[start[0]][start[1]][start_mask] = energy

        pq = [(0, -energy, start[0], start[1], start_mask)]
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while pq:
            d, neg_e, i, j, mask = heapq.heappop(pq)
            e = -neg_e

            if e < best_energy[i][j][mask]:
                continue

            if mask == full_mask:
                return d

            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and classroom[ni][nj] != 'X':
                    if e - 1 < 0:
                        continue
                    ne = e - 1
                    if classroom[ni][nj] == 'R':
                        ne = energy
                    nmask = mask
                    if (ni, nj) in litter_idx:
                        nmask |= (1 << litter_idx[(ni, nj)])

                    if ne > best_energy[ni][nj][nmask]:
                        best_energy[ni][nj][nmask] = ne
                        heapq.heappush(pq, (d + 1, -ne, ni, nj, nmask))

        return -1