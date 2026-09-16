class Solution:
     def fib(self, n: int) -> int:
         def fib(n,a,b):
          if n == 0:
             return a
          return fib(n-1,b,a+b)
         return fib (n,0,1)
        