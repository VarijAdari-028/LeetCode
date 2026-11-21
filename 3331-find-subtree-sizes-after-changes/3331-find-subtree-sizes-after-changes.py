from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        # Phase 1: nearest same-character ancestor in the ORIGINAL tree
        new_parent = parent[:]
        last = [-1] * 26                      # last[c] = nearest ancestor with char c
        stack = [(0, 0)]                      # (node, state) state 0 = enter, 1 = exit
        saved = {}                            # node -> previous last[c] to restore on exit
        while stack:
            u, state = stack.pop()
            c = ord(s[u]) - 97
            if state == 0:
                if u != 0 and last[c] != -1:
                    new_parent[u] = last[c]
                saved[u] = last[c]
                last[c] = u
                stack.append((u, 1))
                for v in children[u]:
                    stack.append((v, 0))
            else:
                last[c] = saved[u]

        # Phase 2: subtree sizes in the new tree
        new_children = [[] for _ in range(n)]
        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        order = []
        st = [0]
        while st:
            u = st.pop()
            order.append(u)
            st.extend(new_children[u])

        size = [1] * n
        for u in reversed(order):
            if u != 0:
                size[new_parent[u]] += size[u]

        return size