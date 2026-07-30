class Solution(object):
    def longestCommonPrefix(self, strs):
        ans = strs[0]

        for s in strs:
            while ans != s[:len(ans)]:
                ans = ans[:-1]

        return ans