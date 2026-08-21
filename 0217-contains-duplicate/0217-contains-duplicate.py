class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = nums
        hash_list = {}
        for nums in n:
         if nums in hash_list:
            return True

         hash_list[nums]=1


        return False
        