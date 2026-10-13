class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        nums.sort(key = lambda x : x*x)
        n = len(nums)
        small = sum(x * x for x in nums [:n//2])
        large = sum(x * x for x in nums [n//2:])

        return large - small
     
        