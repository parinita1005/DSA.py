class Solution:
    def dfs(self, grid, r, c):
        m = len(grid)
        n = len(grid[0])

        # Out of bounds
        if r >= m or r < 0 or c >= n or c < 0:
            return False

        # Water or already visited
        if grid[r][c] == 1:
            return True

        # Mark as visited
        grid[r][c] = 1

        left_closed = self.dfs(grid, r, c - 1)
        right_closed = self.dfs(grid, r, c + 1)
        up_closed = self.dfs(grid, r - 1, c)
        down_closed = self.dfs(grid, r + 1, c)

        return (left_closed and right_closed
                and up_closed and down_closed)

    def closedIsland(self, grid):
        m = len(grid)
        n = len(grid[0])

        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if self.dfs(grid, i, j):
                        count += 1

        return count
        