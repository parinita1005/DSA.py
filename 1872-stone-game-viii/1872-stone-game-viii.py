from itertools import accumulate
class Solution:
    def stoneGameVIII(self, stones: List[int]) -> int:
        prefix = list(accumulate(stones))

        ans = prefix[-1]

        for i in range(len(stones) -2,0,-1):
            ans = max(ans , prefix[i]-ans)

        return ans 
        