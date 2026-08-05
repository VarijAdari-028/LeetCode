from typing import List

class Solution:
    def remainingMethods(
        self, n: int, k: int, invocations: List[List[int]]
    ) -> List[int]:

        graph = [[] for _ in range(n)]

        for a, b in invocations:
            graph[a].append(b)

        # Step 1: Find every suspicious method
        suspicious = [False] * n
        stack = [k]
        suspicious[k] = True

        while stack:
            node = stack.pop()

            for nxt in graph[node]:
                if not suspicious[nxt]:
                    suspicious[nxt] = True
                    stack.append(nxt)

        # Step 2: Check if a non-suspicious method
        # calls a suspicious method
        for a, b in invocations:
            if not suspicious[a] and suspicious[b]:
                # Cannot remove suspicious methods
                return list(range(n))

        # Step 3: Remove suspicious methods
        return [i for i in range(n) if not suspicious[i]]