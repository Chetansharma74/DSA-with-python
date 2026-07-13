from collections import deque

class Solution(object):
    def sequentialDigits(self, low, high):
        q = deque(range(1, 10))
        ans = []

        while q:
            num = q.popleft()

            if low <= num <= high:
                ans.append(num)

            last = num % 10

            if last < 9:
                new_num = num * 10 + last + 1

                if new_num <= high:
                    q.append(new_num)

        return ans