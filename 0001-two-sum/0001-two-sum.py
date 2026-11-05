class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash_map = {}
        n = len(nums)
        for i in range(n):
            remaining = target-nums[i]
            if remaining in hash_map:
                return(hash_map[remaining],i)
            hash_map[nums[i]] = i
        