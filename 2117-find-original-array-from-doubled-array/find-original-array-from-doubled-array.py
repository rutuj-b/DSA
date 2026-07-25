class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        n = len(changed)
        if n%2 != 0: return []

        org = []
        freq = Counter(changed)
        
        if freq[0] % 2 != 0: return []
        org.extend([0] * (freq[0]//2))
        freq[0] = 0

        for num in sorted(changed):
            if freq[num] == 0: continue

            if freq[num] > freq[num*2]:
                return []

            org.extend([num]* freq[num])
            freq[num*2] -= freq[num]
            freq[num] = 0
        return org

