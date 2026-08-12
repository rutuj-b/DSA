class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)
        res = 0 
        odd = False
        
        for count in freq.values():
            if count % 2 == 0 :
                res += count 
            else:
                res += count - 1
                odd = True 
        if odd :
            return res + 1
        return res