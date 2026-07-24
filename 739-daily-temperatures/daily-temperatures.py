class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = [0]*n
        store = []
        for i , temp in enumerate(temperatures):
            while store and temp > temperatures[store[-1]]:
                index = store.pop()
                stack[index] = i - index
            store.append(i)
        return stack