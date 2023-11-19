from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 9:19
    def trap(self, height: List[int]) -> int:
        stack = []
        trapped = 0

        for i in range(len(height)):
            bar = height[i]

            while stack and bar > stack[-1][0]:
                popped, popped_index = stack.pop()

                if not stack:
                    break

                left_bound, index = stack[-1]

                trapped += min(left_bound - popped, bar - popped) * (i - index - 1)

            stack.append((bar, i))

        return trapped
        
solution = Solution()
answer = solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print(answer)