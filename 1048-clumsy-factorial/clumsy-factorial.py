class Solution:
    def clumsy(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 6
        if n == 4:
            return 7

        r = n % 4

        if r == 0:
            return n + 1
        elif r == 1:
            return n + 2
        elif r == 2:
            return n + 2
        else:
            return n - 1