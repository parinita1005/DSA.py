class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n = len(nums)
        total = 0
        maxi = float("-inf")
        for i in range(0,n):
            total = total + nums[i]
            maxi = max(maxi,total)
            if total<0:
                total = 0
        return maxi
        