class Solution:
    def longestSubsequence(self, nums):
        n = len(nums)

        xor = 0

        for num in nums:
            xor ^= num

        if xor != 0:
            return n

        if nums.count(0) == n:
            return 0

        return n - 1