class Solution:
    def removeInvalidParentheses(self, s: str):
        def valid(x):
            b = 0

            for c in x:
                if c == '(':
                    b += 1
                elif c == ')':
                    b -= 1
                    if b < 0:
                        return False

            return b == 0

        q = {s}

        while q:
            ans = [x for x in q if valid(x)]

            if ans:
                return ans

            q = {
                x[:i] + x[i+1:]
                for x in q
                for i in range(len(x))
                if x[i] in "()"
            }
        