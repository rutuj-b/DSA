class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        #CHECK NOTES
        nums = list(map(str, nums))

        def compare(n1 , n2):
            if n1 + n2 > n2 + n1 :
                return -1
            elif n1 + n2 < n2 + n1:
                return 1
            return 0

        nums.sort(key=cmp_to_key(compare))

        return str(int("".join(nums)))
