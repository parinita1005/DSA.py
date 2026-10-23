from typing import List
class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        ans = -1
        for i,x in enumerate(nums):
            if i!=x:
              ans&=x
        return max(ans,0)
      