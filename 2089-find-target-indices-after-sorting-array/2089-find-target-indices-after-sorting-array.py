class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        nums.sort()
       
        return [i for i, x in enumerate(nums) if x == target]
     
     
        