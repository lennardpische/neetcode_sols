class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = {}
        max_len = 0
        for right in range(len(s)):
            c = s[right]
            if c in seen and seen[c] >= left:
                left = seen[c] + 1
            seen[c] = right
            max_len = max(max_len, right - left + 1)
        return int(max_len)
