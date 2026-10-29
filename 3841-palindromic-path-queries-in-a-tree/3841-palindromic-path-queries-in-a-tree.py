from typing import List

class Solution:
    def palindromePath(self, n: int, edges: List[List[int]], s: str, queries: List[str]) -> List[bool]:
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        LOG = n.bit_length()
        tin = [0] * n
        tout = [0] * n
        up = [[0] * n for _ in range(LOG)]
        timer = 0

        stack = [(0, 0, 0)]
        while stack:
            u, p, state = stack.pop()

            if state == 0:
                tin[u] = timer
                timer += 1
                up[0][u] = p

                for k in range(1, LOG):
                    up[k][u] = up[k - 1][up[k - 1][u]]

                stack.append((u, p, 1))
                for v in reversed(g[u]):
                    if v != p:
                        stack.append((v, u, 0))
            else:
                tout[u] = timer

        def is_ancestor(u, v):
            return tin[u] <= tin[v] < tout[u]

        def lca(u, v):
            if is_ancestor(u, v):
                return u
            if is_ancestor(v, u):
                return v

            for k in range(LOG - 1, -1, -1):
                if not is_ancestor(up[k][u], v):
                    u = up[k][u]

            return up[0][u]

        bit = [0] * (n + 1)

        def add(i, x):
            i += 1
            while i <= n:
                bit[i] ^= x
                i += i & -i

        def range_update(u, x):
            add(tin[u], x)
            if tout[u] < n:
                add(tout[u], x)

        def prefix(i):
            res = 0
            while i:
                res ^= bit[i]
                i -= i & -i
            return res

        chars = list(s)

        for u, c in enumerate(chars):
            range_update(u, 1 << (ord(c) - ord('a')))

        ans = []

        for q in queries:
            parts = q.split()
            u = int(parts[1])

            if parts[0] == "update":
                c = parts[2]

                delta = (1 << (ord(chars[u]) - ord('a'))) ^ (1 << (ord(c) - ord('a')))
                range_update(u, delta)
                chars[u] = c

            else:
                v = int(parts[2])
                w = lca(u, v)

                mask = prefix(tin[u] + 1) ^ prefix(tin[v] + 1)
                mask ^= 1 << (ord(chars[w]) - ord('a'))

                ans.append(mask == 0 or (mask & (mask - 1)) == 0)

        return ans