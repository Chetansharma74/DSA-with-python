class Solution(object):
    def lengthOfLongestSubstring(self, s):
        st = set()
        L = 0
        max_len = 0

        for r in range(len(s)):
            while s[r] in st:
                st.remove(s[L])
                L += 1

            st.add(s[r])
            max_len = max(max_len, r - L + 1)

        return max_len