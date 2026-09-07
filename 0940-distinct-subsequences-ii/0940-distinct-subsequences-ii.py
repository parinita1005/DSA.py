
class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        # dp[i] = number of distinct subsequences (including empty)
        # using the first i characters
        dp = [0] * (n + 1)
        dp[0] = 1

        # Last occurrence of each character
        last = {}

        for i in range(1, n + 1):
            c = s[i - 1]

            # Every existing subsequence can either take or skip c
            dp[i] = (2 * dp[i - 1]) % MOD

            # Remove duplicates created by previous occurrence of c
            if c in last:
                dp[i] = (dp[i] - dp[last[c] - 1]) % MOD

            # Store current occurrence
            last[c] = i

        # Remove the empty subsequence
        return (dp[n] - 1) % MOD

        