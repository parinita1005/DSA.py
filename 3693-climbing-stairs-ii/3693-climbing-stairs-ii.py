class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float("inf")]*(n+1) #construct kra dp array
        dp[0] = 0 #start kra iska kpoi charge nahi tha
        for i in range(1,n+1):
            for j in range(max(0,i-3),i): #help karega previous pe na jae
                dp[i] = min(dp[i],dp[j]+costs[i-1]+(i-j)**2) #j previous ki cost hai cost i-j current ka price hai and jump hai 2 squres.

        return dp[n] #it will return it all.
        