class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char = {}
        left = 0
        max_length = 0
        for right in range(len(s)):
            if s[right] in char and char[s[right]] >= left:
                left = char[s[right]] + 1
            char[s[right]] = right
            current_length = right - left + 1
            max_length = max(max_length, current_length)
        return max_length