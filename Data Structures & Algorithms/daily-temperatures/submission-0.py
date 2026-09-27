class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = [] # pair: [temp, idx]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stack_t, stack_idx = stack.pop()
                result[stack_idx] = i - stack_idx
            stack.append([t, i])
        return result 
        