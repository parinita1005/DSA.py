class Solution:
    def isPalindrome(self, s: str) -> bool:
        # l=0
        # r=len(s)-1
        s=s.lower()
        def Palindrome(l,r):
            if l>=r:
                return True
            
            
            if not s[l].isalnum():
                return Palindrome(l+1,r)
            if not s[r].isalnum():
                return Palindrome(l,r-1)
            
            if s[l]!=s[r]:
                return False
            return Palindrome(l+1,r-1)
        return Palindrome(0,len(s)-1)
        