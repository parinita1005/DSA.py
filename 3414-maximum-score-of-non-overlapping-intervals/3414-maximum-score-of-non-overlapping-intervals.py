from bisect import bisect_right

class Solution:
    def maximumWeight(self, intervals):
        n = len(intervals)

        # Store: [left, right, weight, original_index]
        arr = []
        for i, (l, r, w) in enumerate(intervals):
            arr.append([l, r, w, i])

        # Sort by starting position
        arr.sort()

        starts = [x[0] for x in arr]

        # dp[i][k] = best result using intervals from i onward,
        # choosing at most k intervals
        dp = [[None] * 5 for _ in range(n + 1)]

        def solve(i, k):
            if i == n or k == 0:
                return (0, [])

            if dp[i][k] is not None:
                return dp[i][k]

            # Option 1: skip current interval
            score1, indices1 = solve(i + 1, k)

            l, r, w, original_index = arr[i]

            # Find first interval whose start > r
            # because sharing boundary means overlapping
            j = bisect_right(starts, r)

            # Option 2: take current interval
            score2, indices2 = solve(j, k - 1)
            score2 += w

            indices2 = indices2 + [original_index]
            indices2.sort()

            # Choose the better answer
            if score2 > score1:
                ans = (score2, indices2)
            elif score2 < score1:
                ans = (score1, indices1)
            else:
                # Same score → lexicographically smaller indices
                ans = (score2, min(indices1, indices2))

            dp[i][k] = ans
            return ans

        return solve(0, 4)[1]