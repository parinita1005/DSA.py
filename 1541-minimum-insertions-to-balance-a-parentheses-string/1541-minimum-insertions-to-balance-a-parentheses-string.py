class Solution:
    def minInsertions(self, s: str) -> int:
        balance = 0
        insertion = 0
        for ch in s:
            if ch == '(':
                balance+=2
                if balance%2 == 1:
                 insertion+=1
                 balance-=1
            else:
                balance -=1
                if balance<0:
                    insertion+=1
                    balance=1
        return insertion+balance
       
        