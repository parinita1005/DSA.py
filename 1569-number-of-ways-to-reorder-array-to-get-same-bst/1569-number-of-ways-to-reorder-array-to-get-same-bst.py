from math import comb
class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        mod = 10**9+7
        def dfs(nums):
            n = len(nums)
            if n<3:
                return 1
            left_node = [a for a in nums if a<nums[0]]
            right_node = [a for a in nums if a>nums[0]]
            return dfs(left_node)*dfs(right_node)*comb(n-1,len(left_node))%mod
        return (dfs(nums)-1)%mod
        