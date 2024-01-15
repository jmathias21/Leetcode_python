from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 11:11
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        stack = []

        for interval in intervals:
            if not stack or interval[0] > stack[-1][1]:
                stack.append(interval)
            else:
                stack[-1][1] = max(stack[-1][1], interval[1])

        return stack


        
solution = Solution()
answer = solution.merge([[1,3],[2,6],[8,10],[15,18]])
print(answer)