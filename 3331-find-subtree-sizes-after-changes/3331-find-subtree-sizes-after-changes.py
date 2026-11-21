
class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:

        n = len(parent)

        children = [[] for _ in range(n)]

        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        last = {}

        def dfs(node):
            char = s[node]
            old = last.get(char)

            if old is not None:
                new_parent[node] = old

            last[char] = node

            for child in children[node]:
                dfs(child)

            if old is None:
                del last[char]
            else:
                last[char] = old

        dfs(0)

        new_children = [[] for _ in range(n)]

        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        answer = [0] * n

        def calculate(node):
            answer[node] = 1

            for child in new_children[node]:
                calculate(child)
                answer[node] += answer[child]

        calculate(0)

        return answer

        