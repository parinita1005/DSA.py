class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp =[0]*(n+1)
        pal = [False]*n
        for i in range(n):
            dp[i+1]=dp[i]
            for j in range (i+1):
                if s[j]==s[i] and (i-j<=2 or pal[j+1]):
                    pal[j]=True
                    length = i-j+1
                    if length >=k:
                        dp[i+1]=max(dp[i+1],dp[j]+1)
                else:
                    pal[j]=False
        return dp[n] 