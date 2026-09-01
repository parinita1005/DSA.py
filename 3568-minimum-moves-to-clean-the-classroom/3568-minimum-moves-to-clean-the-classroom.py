from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:

        m, n = len(classroom), len(classroom[0])

        litter_id = {}
        start = None

        for r in range(m):
            for c in range(n):
                if classroom[r][c] == 'S':
                    start = (r, c)
                elif classroom[r][c] == 'L':
                    litter_id[(r, c)] = len(litter_id)

        total_litter = len(litter_id)

        if total_litter == 0:
            return 0

        target_mask = (1 << total_litter) - 1

        sr, sc = start

        # (row, col, mask, energy)
        q = deque([(sr, sc, 0, energy)])

        # For each (r, c, mask), store maximum energy reached.
        best = {(sr, sc, 0): energy}

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        moves = 0

        while q:

            for _ in range(len(q)):

                r, c, mask, e = q.popleft()

                if mask == target_mask:
                    return moves

                if e == 0:
                    continue

                for dr, dc in directions:

                    nr = r + dr
                    nc = c + dc

                    # Outside grid
                    if nr < 0 or nr >= m or nc < 0 or nc >= n:
                        continue

                    # Wall
                    if classroom[nr][nc] == 'X':
                        continue

                    new_energy = e - 1
                    new_mask = mask

                    # Collect litter
                    if (nr, nc) in litter_id:
                        bit = litter_id[(nr, nc)]
                        new_mask |= 1 << bit

                    # Recharge
                    if classroom[nr][nc] == 'R':
                        new_energy = energy

                    key = (nr, nc, new_mask)

                    # Only keep this state if it has MORE energy
                    # than anything we've seen before.
                    if new_energy > best.get(key, -1):
                        best[key] = new_energy
                        q.append((nr, nc, new_mask, new_energy))

            moves += 1

        return -1
        