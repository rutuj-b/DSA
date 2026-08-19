class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        minn = float('INF')
        for price in prices:
            minn = min(minn , price)
            maxx= max(maxx , price - minn)
        return maxx