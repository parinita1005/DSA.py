class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        result = [0] * k
        dp = [0] * k

        for num in nums:
            new_dp = [0] * k

            # Subarray containing only num
            remainder = num % k
            new_dp[remainder] += 1

            # Extend previous subarrays
            for r in range(k):
                if dp[r] > 0:
                    new_remainder = (r * num) % k
                    new_dp[new_remainder] += dp[r]

            # Add current subarrays to answer
            for r in range(k):
                result[r] += new_dp[r]

            dp = new_dp

        return result
        