class Solution(object):
    def checkDivisibility(self, n):

           num = n
           digit_sum = 0
           digit_product = 1

           while num > 0:

            ld = num % 10

            digit_sum+=ld
            digit_product*=ld

            num//=10

           if (n % (digit_sum + digit_product)==0 ):
                return True
           else:
                return False