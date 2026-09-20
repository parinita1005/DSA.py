class Solution:
    def reverseDegree(self, s: str) -> int:
        total = 0
        for idx,ch in enumerate(s,1):
      
         reverse = 26-(ord(ch)-ord('a'))

         total+=(reverse*idx)
        return total
      

        