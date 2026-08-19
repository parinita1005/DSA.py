class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        sign = -1 if x<0 else 1
        num =abs( x)
        result=0
     
   
        #  for i in range(1,num+1):
        while num>0:
          
            ld=num%10
            num=num//10

            result = (result*10)+ld
        result = result*sign
      
        if result < -2147483648 or result > 2147483647:
            return 0

        return result
