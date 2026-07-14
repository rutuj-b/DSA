class Solution:
    def sortVowels(self, s: str) -> str:
        s = list(s)
        vowels = set('AEIOUaeiou')
       
        vowel_char = [ch for ch in s if ch in vowels]
        vowel_char.sort()
        j = 0
        for i , ch in enumerate(s):
            if ch in vowels:
                s[i] = vowel_char[j]
                j += 1
        return "".join(s)


        
