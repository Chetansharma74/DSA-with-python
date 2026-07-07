class Solution(object):
    def sumAndMultiply(self, n):
        digits = []

        for ch in str(n):
            if ch != '0':
                digits.append(ch)

        if not digits:
            return 0

        x = int("".join(digits))
        digit_sum = 0

        for d in digits:
            digit_sum += int(d)

        return x * digit_sum