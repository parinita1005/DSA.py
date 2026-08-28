class Solution:
  def lexPalindromicPermutation(self, s: str, target: str) -> str:
    n = len(s)
    count = [0] * 26
    for ch in s:
        count[ord(ch) - 97] += 1

    # Cannot form a palindrome
    if sum(x % 2 for x in count) > 1:
        return ""

    half = []
    mid = ""

    for i in range(26):
        half += [chr(i + 97)] * (count[i] // 2)
        if count[i] % 2:
            mid = chr(i + 97)

    half = ''.join(half)
    m = len(half)
    ans = ""

    # Smallest possible palindrome
    pal = half + mid + half[::-1]
    if pal > target:
        ans = pal

    # IMPORTANT:
    # Try using target's left half exactly.
    equal_left = target[:m]
    need = [0] * 26

    for ch in equal_left:
        need[ord(ch) - 97] += 1

    if all(need[i] <= count[i] // 2 for i in range(26)):
        pal = equal_left + mid + equal_left[::-1]

        if pal > target and (not ans or pal < ans):
            ans = pal

    # Try making the left half strictly greater
    for i in range(m - 1, -1, -1):
        used = [0] * 26
        prefix = []

        ok = True

        # Match target before position i
        for j in range(i):
            x = ord(target[j]) - 97
            used[x] += 1

            if used[x] > count[x] // 2:
                ok = False
                break

            prefix.append(target[j])

        if not ok:
            continue

        # Choose smallest character > target[i]
        for c in range(ord(target[i]) - 96, 26):
            if used[c] < count[c] // 2:

                left = ''.join(prefix) + chr(c + 97)

                # Fill remaining characters smallest-first
                rem = []

                for x in range(26):
                    k = count[x] // 2 - used[x]

                    if x == c:
                        k -= 1

                    rem += [chr(x + 97)] * k

                left += ''.join(rem)

                palindrome = left + mid + left[::-1]

                if not ans or palindrome < ans:
                    ans = palindrome

                break

    return ans



