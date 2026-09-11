class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        ans = set()

        for i in range(len(digits)):
            for j in range(len(digits)):
                for k in range(len(digits)):
                    
                    # Each copy can be used only once
                    if i == j or j == k or i == k:
                        continue

                    # First digit cannot be 0
                    if digits[i] == 0:
                        continue

                    # Last digit must be even
                    if digits[k] % 2 != 0:
                        continue

                    number = digits[i] * 100 + digits[j] * 10 + digits[k]
                    ans.add(number)

        return len(ans)