class Solution:
    def nthUglyNumber(self, n: int) -> int:
        uglyno = [1]
        twopos = threepos = fivepos = 0
        while len(uglyno) < n :
            bytwo = uglyno[twopos] * 2
            bythree = uglyno[threepos] * 3
            byfive = uglyno[fivepos] * 5

            minimum = min(bytwo, bythree , byfive)

            uglyno.append(minimum)

            if minimum == bytwo : twopos += 1
            if minimum == bythree : threepos += 1
            if minimum == byfive : fivepos += 1
        return uglyno[-1]