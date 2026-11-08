class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0]*n
        posIndex,negIndex = 0,1
        for i in range(0,n):
            if nums[i]>=0:
                result [posIndex]=nums[i]
                posIndex+=2
            else:
                result[negIndex] = nums[i]
                negIndex+=2
        return result
        