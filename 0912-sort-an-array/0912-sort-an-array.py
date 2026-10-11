class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
      if len(nums)<=1:
        return nums
      mid = len(nums)//2
      left_half = nums [:mid]
      right_half = nums [mid:]
      left_half = self.sortArray(left_half)
      right_half = self.sortArray(right_half)
      return self.merge (left_half,right_half)
    
    def merge(self,left,right):
        result = []
        i,j = 0,0
        n,m = len(left),len(right)
        while i<n and j < m:
            if left[i]<=right[j]:
                result.append(left[i])
                i+=1
            else:
                result.append(right[j])
                j+=1
        result.extend(left[i:])  
        result.extend(right[j:])
        return result
