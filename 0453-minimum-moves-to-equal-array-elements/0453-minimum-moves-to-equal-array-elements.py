class Solution:
    def minMoves(self, nums: list[int]) -> int:
        n = len(nums)
        min_element = min(nums)
        moves = 0
        for i in range(n):
            moves += nums[i] - min_element
        return moves
 
       

        