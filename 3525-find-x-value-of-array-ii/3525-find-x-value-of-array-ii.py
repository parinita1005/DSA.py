class Solution:
    def resultArray(self, nums, k, queries):

        n = len(nums)

        # tree[node] = [product, counts]
        #
        # product = product of the whole segment % k
        #
        # counts[r] = number of non-empty prefixes
        #             whose product % k == r
        tree = [(1, [0] * k) for _ in range(4 * n)]

        # --------------------------------------------------
        # MERGE TWO NODES
        # --------------------------------------------------
        def merge(left, right):

            left_product, left_count = left
            right_product, right_count = right

            # Product of complete combined segment
            product = (left_product * right_product) % k

            count = left_count[:]

            # Prefixes which use the complete left segment
            # and then a prefix of the right segment
            for r in range(k):
                if right_count[r]:
                    new_remainder = (left_product * r) % k
                    count[new_remainder] += right_count[r]

            return product, count

        # --------------------------------------------------
        # BUILD SEGMENT TREE
        # --------------------------------------------------
        def build(node, l, r):

            if l == r:
                remainder = nums[l] % k

                count = [0] * k
                count[remainder] = 1

                tree[node] = (remainder, count)
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        # --------------------------------------------------
        # UPDATE
        # --------------------------------------------------
        def update(node, l, r, index, value):

            if l == r:

                remainder = value % k

                count = [0] * k
                count[remainder] = 1

                tree[node] = (remainder, count)
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, r, index, value)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        # --------------------------------------------------
        # RANGE QUERY
        # --------------------------------------------------
        def query(node, l, r, ql, qr):

            # Completely inside query range
            if ql <= l and r <= qr:
                return tree[node]

            mid = (l + r) // 2

            # Completely in left side
            if qr <= mid:
                return query(
                    node * 2,
                    l,
                    mid,
                    ql,
                    qr
                )

            # Completely in right side
            if ql > mid:
                return query(
                    node * 2 + 1,
                    mid + 1,
                    r,
                    ql,
                    qr
                )

            # Query overlaps both sides
            left = query(
                node * 2,
                l,
                mid,
                ql,
                qr
            )

            right = query(
                node * 2 + 1,
                mid + 1,
                r,
                ql,
                qr
            )

            return merge(left, right)

        # Build initially
        build(1, 0, n - 1)

        answer = []

        # --------------------------------------------------
        # PROCESS QUERIES
        # --------------------------------------------------
        for index, value, start, x in queries:

            # 1. Permanently update nums[index]
            nums[index] = value

            update(
                1,
                0,
                n - 1,
                index,
                value
            )

            # 2. Consider nums[start ... n-1]
            product, count = query(
                1,
                0,
                n - 1,
                start,
                n - 1
            )

            # 3. count[x] = number of valid ways
            answer.append(count[x])

        return answer

        