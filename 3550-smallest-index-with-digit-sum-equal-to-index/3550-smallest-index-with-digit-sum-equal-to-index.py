class Solution:
    def smallestIndex(self, nums: List[int],) -> int:
        for idx,num in enumerate(nums):
            digit_sum = sum(int(digit)for digit in str(num))
            if digit_sum == idx:
                 return idx
        return -1
         
         
           
            
            
       
        