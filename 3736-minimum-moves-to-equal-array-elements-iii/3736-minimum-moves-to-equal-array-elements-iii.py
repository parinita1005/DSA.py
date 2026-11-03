class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n = len(nums)
        moves = 0
        max_element = max(nums)
        for i in range(n):
            while nums[i]!=max_element:
                nums[i]+=1
                moves+=1
        return moves
        