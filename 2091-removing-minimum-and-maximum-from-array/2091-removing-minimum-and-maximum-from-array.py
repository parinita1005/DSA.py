class Solution:
    def minimumDeletions(self, nums):
        n = len(nums)

        min_index = nums.index(min(nums))
        max_index = nums.index(max(nums))

        # Make min_index the smaller index
        left = min(min_index, max_index)
        right = max(min_index, max_index)

        # 3 possibilities:
        # 1. Remove both from the front
        # 2. Remove both from the back
        # 3. Remove left from front and right from back

        front = right + 1
        back = n - left
        both = (left + 1) + (n - right)

        return min(front, back, both)
        