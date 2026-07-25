class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sort = sorted(nums)
        count = {}
        for i , num in enumerate(sort):
            if num not in count :
                count[num] = i

        return [count[num] for num in nums]
