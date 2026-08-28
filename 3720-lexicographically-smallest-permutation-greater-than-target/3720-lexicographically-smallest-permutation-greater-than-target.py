class Solution:
    def lexGreaterPermutation(self, s: str, target: str) -> str:
        
        # Count characters in s
        count = [0] * 26

        for ch in s:
            count[ord(ch) - ord('a')] += 1

        prefix = []

        # Try to match target from left to right
        for i in range(len(target)):
            
            idx = ord(target[i]) - ord('a')

            # We can use the same character
            if count[idx] > 0:
                prefix.append(target[i])
                count[idx] -= 1

            else:
                # Find smallest character greater than target[i]
                for j in range(idx + 1, 26):
                    
                    if count[j] > 0:
                        prefix.append(chr(j + ord('a')))
                        count[j] -= 1

                        # Put remaining characters in sorted order
                        for k in range(26):
                            prefix.extend(
                                [chr(k + ord('a'))] * count[k]
                            )

                        return ''.join(prefix)

                # No bigger character found
                break

        # Backtrack from right to left
        for i in range(len(prefix) - 1, -1, -1):

            # Put prefix[i] back into count
            current = ord(prefix[i]) - ord('a')
            count[current] += 1

            # Find smallest character greater than prefix[i]
            for j in range(current + 1, 26):

                if count[j] > 0:

                    # Keep everything before i
                    answer = prefix[:i]

                    # Put the bigger character
                    answer.append(chr(j + ord('a')))
                    count[j] -= 1

                    # Add remaining characters in sorted order
                    for k in range(26):
                        answer.extend(
                            [chr(k + ord('a'))] * count[k]
                        )

                    return ''.join(answer)

        # No permutation is greater than target
        return ""