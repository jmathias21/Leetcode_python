from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 4:17
    def trap(self, height: List[int]) -> int:
        stack = []
        trapped = 0

        for i, bar in enumerate(height):
            while stack and bar >= stack[-1][0]:
                popped_height, _ = stack.pop()

                if not stack:
                    break

                dist = i - stack[-1][1] - 1
                trapped += dist * (min(stack[-1][0], bar) - popped_height)

            stack.append((bar, i))
            print('trapped: ' + str(trapped))

        return trapped


        
solution = Solution()
answer = solution.trap([0,1,0,2,1,0,1,3,2,1,2,1])
print(answer)