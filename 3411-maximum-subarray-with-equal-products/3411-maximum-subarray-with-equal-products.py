from math import prod,lcm,gcd
class Solution:
    def maxLength(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i,n):
                sub = nums[i:j+1]
      
                if prod(sub) == lcm(*sub) * gcd(*sub):
                    ans = max(ans,len(sub))
          
        return ans
        
        