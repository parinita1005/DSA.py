
from typing import List

class Solution:
    def sortableIntegers(self, nums: List[int]) -> int:
        n = len(nums)
        target = sorted(nums)
        ans = 0

        def is_rotation(a, b):
            k = len(a)
            doubled = a + a

            # Build KMP prefix table
            lps = [0] * k
            j = 0

            for i in range(1, k):
                while j > 0 and b[i] != b[j]:
                    j = lps[j - 1]

                if b[i] == b[j]:
                    j += 1

                lps[i] = j

            # Search b in a + a
            j = 0

            for i in range(2 * k - 1):
                while j > 0 and doubled[i] != b[j]:
                    j = lps[j - 1]

                if doubled[i] == b[j]:
                    j += 1

                if j == k:
                    return True

            return False

        for k in range(1, n + 1):
            if n % k != 0:
                continue

            valid = True

            for start in range(0, n, k):
                a = nums[start:start + k]
                b = target[start:start + k]

                if not is_rotation(a, b):
                    valid = False
                    break

            if valid:
                ans += k

        return ans




        