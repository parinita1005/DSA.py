
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        MOD = 10**9 + 7

        odd = 0
        even = 1
        total = 0
        count = 0

        for num in arr:
            total += num

            if total % 2 == 0:
                count += odd
                even += 1
            else:
                count += even
                odd += 1

        return count % MOD
