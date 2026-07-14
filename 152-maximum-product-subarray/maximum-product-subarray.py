class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        leftproduct = 1
        rightproduct = 1
        res = nums[0]
        n = len(nums)
        for i in range(n):
            if leftproduct == 0 :
                leftproduct = 1
            if rightproduct == 0: 
                rightproduct = 1
            leftproduct *= nums[i]
            rightproduct *= nums[n - i - 1]
            res = max(leftproduct  , rightproduct , res)
        return res
        