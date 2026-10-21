class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        if list(s) == sorted(s):
            return 0
        if (n==2):
            return -1
        min_char = min(s)
        max_char = max(s)

        if (s[0] ==min_char or s[n-1] == max_char):
            return 1

        max_mid = max(s[1:n-1],default ='')
        min_mid = min(s[1:n-1],default ='')

        if (s[0]> max_mid and s[n-1]<min_mid):
            return 3
        return 2

        


        