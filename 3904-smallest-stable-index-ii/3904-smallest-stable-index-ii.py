
class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        # suffix_min[i] = minimum value from nums[i] to nums[n - 1]
        suffix_min = [0] * n
        suffix_min[n - 1] = nums[n - 1]

        for i in range(n - 2, -1, -1):
            suffix_min[i] = min(nums[i], suffix_min[i + 1])

        # prefix_max = maximum value from nums[0] to nums[i]
        prefix_max = nums[0]

        # Check indices from left to right
        for i in range(n):
            prefix_max = max(prefix_max, nums[i])

            # instability score
            score = prefix_max - suffix_min[i]

            if score <= k:
                return i

        return -1


        