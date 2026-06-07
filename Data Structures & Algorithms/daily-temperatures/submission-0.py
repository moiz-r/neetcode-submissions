class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temps)
        for i in range(len(temps)):
            
            while len(stack) > 0 and temps[stack[-1]] < temps[i]:
                remove_idx = stack.pop()
                res[remove_idx] = i - remove_idx
            stack.append(i)

        return res
