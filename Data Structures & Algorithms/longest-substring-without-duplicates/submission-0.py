class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        curr_substr = s[0]
        max_length = 1
        L = 0
        R = 0
        while R < len(s) - 1:
            R += 1
            while s[R] in curr_substr:
                L = L + 1
                curr_substr = s[L:R]
            curr_substr = s[L:R+1]
            max_length = max(max_length, len(curr_substr))
        return max_length
