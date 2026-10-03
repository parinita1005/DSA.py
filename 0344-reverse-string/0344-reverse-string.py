class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.

        """
        def reverse(s,l,r):
             if l>=r:
                return
             s[l],s[r]=s[r],s[l]
             reverse(s,l+1,r-1)
        reverse(s,0,len(s)-1)
        
     

        