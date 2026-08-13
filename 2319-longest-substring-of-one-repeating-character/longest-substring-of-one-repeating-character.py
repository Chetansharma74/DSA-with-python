class Solution:
    def longestRepeating(self, s, queryCharacters, queryIndices):
        n = len(s)

        # Tree stores:
        # left character, right character,
        # prefix length, suffix length, maximum length
        tree = [None] * (4 * n)

        def merge(a, b):
            if a is None:
                return b
            if b is None:
                return a

            left_char = a[0]
            right_char = b[1]

            prefix = a[2]
            suffix = b[3]
            maximum = max(a[4], b[4])

            # If right end of left part == left end of right part
            if a[1] == b[0]:
                if a[2] == a[5]:
                    prefix = a[2] + b[2]

                if b[3] == b[5]:
                    suffix = b[3] + a[3]

                maximum = max(maximum, a[3] + b[2])

            return (left_char, right_char, prefix, suffix, maximum,
                    a[5] + b[5])

        def build(node, l, r):
            if l == r:
                tree[node] = (s[l], s[l], 1, 1, 1, 1)
                return

            mid = (l + r) // 2

            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        def update(node, l, r, index, char):
            if l == r:
                tree[node] = (char, char, 1, 1, 1, 1)
                return

            mid = (l + r) // 2

            if index <= mid:
                update(node * 2, l, mid, index, char)
            else:
                update(node * 2 + 1, mid + 1, r, index, char)

            tree[node] = merge(
                tree[node * 2],
                tree[node * 2 + 1]
            )

        build(1, 0, n - 1)

        ans = []

        for i in range(len(queryCharacters)):
            index = queryIndices[i]
            char = queryCharacters[i]

            update(1, 0, n - 1, index, char)

            # maximum repeating substring is stored at root
            ans.append(tree[1][4])

        return ans