class BIT:
    def __init__(self, n: int):
        self.size = n
        self._tree1 = defaultdict(int)
        self._tree2 = defaultdict(int)

    def _lowbit(self, index: int) -> int:
        return index & -index

    def add(self, left: int, right: int, delta: int) -> None:
        self._add(left, delta)
        self._add(right + 1, -delta)

    def query(self, left: int, right: int) -> int:
        return self._query(right) - self._query(left - 1)

    def _add(self, index: int, delta: int) -> None:
        index += 1
        rawIndex = index
        while index <= self.size:
            self._tree1[index] += delta
            self._tree2[index] += (rawIndex - 1) * delta
            index += self._lowbit(index)

    def _query(self, index: int) -> int:
        index += 1
        rawIndex = index
        res = 0
        while index > 0:
            res += rawIndex * self._tree1[index] - self._tree2[index]
            index -= self._lowbit(index)
        return res

class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        n = len(nums)
        bit = BIT(n)
        seen = {}
        cur = res = 0
        MOD = 10**9 + 7
        
        for i, a in enumerate(nums):
            j = seen.get(a, -1) + 1
            x_sum = bit.query(j, i)
            total_increase = (2 * x_sum + (i - j + 1)) % MOD
            cur = (cur + total_increase) % MOD
            res = (res + cur) % MOD
            bit.add(j, i, 1)
            seen[a] = i
            
        return res
        