class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        breaks = 0 
        pivot = -1
        for i in range(1 , len(nums)):
            if nums[i] < nums[i-1]:
                breaks += 1
                pivot = i
        if breaks == 0 : return 0
        if breaks > 1 or nums[-1] > nums[0]:
                return -1
        return len(nums) - pivot