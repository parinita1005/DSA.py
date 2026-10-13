class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        even = 0
        odd = 0
        for num in nums:
            old_even = even 
            old_odd = odd

            even = max(old_even,old_odd+num)
            odd = max(old_odd,old_even-num)
        return even