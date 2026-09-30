class Solution:
    def hasValidPath(self, grid):
        m = len(grid)
        n = len(grid[0])

        # Path length must be even
        if (m + n - 1) % 2 != 0:
            return False

        # Start must be '('
        if grid[0][0] == ')':
            return False

        # End must be ')'
        if grid[m - 1][n - 1] == '(':
            return False

        # dp[j] stores all possible balances as bits
        dp = [0] * n

        for i in range(m):
            for j in range(n):

                # Starting cell
                if i == 0 and j == 0:
                    dp[j] = 1 << 1
                    continue

                # Get possible balances from top
                states = dp[j]

                # Get possible balances from left
                if j > 0:
                    states |= dp[j - 1]

                if grid[i][j] == '(':
                    # Increase balance by 1
                    dp[j] = states << 1
                else:
                    # Decrease balance by 1
                    dp[j] = states >> 1

        # Bit 0 = balance 0
        return (dp[n - 1] & 1) != 0

        