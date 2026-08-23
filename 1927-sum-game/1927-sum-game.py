class Solution(object):
    def sumGame(self, num):
        n = len(num)
        half = n // 2

        left_sum = 0
        right_sum = 0

        left_q = 0
        right_q = 0

        # First half
        for i in range(half):
            if num[i] == '?':
                left_q += 1
            else:
                left_sum += int(num[i])

        # Second half
        for i in range(half, n):
            if num[i] == '?':
                right_q += 1
            else:
                right_sum += int(num[i])

        # Same number of '?' on both sides
        if left_q == right_q:
            return left_sum != right_sum

        # Odd difference in '?' means Alice can force inequality
        if (left_q - right_q) % 2 != 0:
            return True

        # Even difference
        difference = left_sum - right_sum
        required = (right_q - left_q) // 2 * 9

        return difference != required
        