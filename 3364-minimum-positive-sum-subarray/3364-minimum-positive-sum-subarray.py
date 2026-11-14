class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        n = len(nums)
        ans = float("inf")
        for i in range(0,n):
            for j in range(i,n):
                subarray = j - i + 1
                if l <= subarray <= r:
                    current_sum = sum(nums[i:j+1])

                    if current_sum>0:
                       ans = min(ans,current_sum)
        return ans if ans!= float("inf") else -1
        
        