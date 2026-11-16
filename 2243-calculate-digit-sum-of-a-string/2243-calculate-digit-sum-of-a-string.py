
class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            result = ""

            for i in range(0, len(s), k):
                group = s[i:i+k]

                digi_sum = 0
                for digit in group:
                    digi_sum += int(digit)

                result += str(digi_sum)

            s = result

        return s



        