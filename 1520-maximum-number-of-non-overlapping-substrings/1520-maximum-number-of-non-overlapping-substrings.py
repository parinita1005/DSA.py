class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        first = {}
        last = {}

        for i, ch in enumerate(s):
            if ch not in first:
                first[ch] = i
            last[ch] = i

        intervals = []

        for ch in first:
            l, r = first[ch], last[ch]
            i = l

            while i <= r:
                c = s[i]

                if first[c] < l:
                    break

                r = max(r, last[c])
                i += 1
            else:
                intervals.append((l, r))

        intervals.sort(key=lambda x: x[1])

        ans = []
        end = -1

        for l, r in intervals:
            if l > end:
                ans.append(s[l:r + 1])
                end = r

        return ans
        