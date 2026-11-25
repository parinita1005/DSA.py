class Solution:
    def smallestUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        base = 1000003
        mask = (1 << 64) - 1

        def check(k):
            freq = {}
            h = 0
            power = pow(base, k - 1, 1 << 64)

            for i in range(k):
                h = (h * base + nums[i]) & mask

            freq[h] = 1

            for i in range(k, n):
                h = (h - nums[i-k] * power) & mask
                h = (h * base + nums[i]) & mask
                freq[h] = freq.get(h, 0) + 1

            return any(v == 1 for v in freq.values())

        left = 1
        right = n

        while left < right:
            mid = (left + right) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1

        return left
        