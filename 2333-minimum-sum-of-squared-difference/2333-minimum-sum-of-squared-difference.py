class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        n = len(nums1)
        countDiff = [0] * 100001
        k = k1+k2
        for i in range(n):
            d = abs(nums1[i]-nums2[i])
            countDiff[d]+=1
        currDiff = 100000
        while currDiff > 0 and k > 0:
            countops = min(countDiff[currDiff], k)

            countDiff[currDiff] -= countops
            countDiff[currDiff - 1] += countops

            k -= countops
            currDiff -= 1

        result = 0

        for d in range(1, 100001):
            result += countDiff[d] * (d * d)

        return result    