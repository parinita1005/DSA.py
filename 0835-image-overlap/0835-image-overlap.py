class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n = len(A)
        maxOverlap = 0
       

        for rowOff in range(-n+1, n):
            for colOff in range(-n+1,n):

                 count = 0
     

                 for i in range(n):
                   for j in range(n):
                       B_i = i + rowOff
                       B_j = j + colOff

                       if B_i < 0 or B_i >=n or B_j <0 or B_j >=n:
                         continue
                       if A[i][j] ==  1 and B[B_i][B_j] == 1:
                         count+=1
               

                 maxOverlap = max(maxOverlap,count)
        return maxOverlap




        
         

        