class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = res = 0 
        char = set()
        for right in range(len(s)):
            while s[right] in char :
                char.remove(s[left])
                left += 1
            char.add(s[right])
            res = max(res , right - left + 1)
        return res