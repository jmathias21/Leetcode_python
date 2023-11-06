from collections import deque
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 24:00
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        output = []
        i = len(asteroids) - 1
        while i >= 0:
            if asteroids[i] < 0:
                output.append(asteroids[i])
            else:
                keep_asteroid = True
                while output:
                    if output[-1] > 0:
                        break
                    elif asteroids[i] > abs(output[-1]):
                        output.pop()
                    elif asteroids[i] == abs(output[-1]):
                        output.pop()
                        keep_asteroid = False
                        break
                    else:
                        keep_asteroid = False
                        break

                if keep_asteroid:
                    output.append(asteroids[i])
            i -= 1

        output.reverse()
        return output


        
solution = Solution()
answer = solution.asteroidCollision([5,10,-5])
answer = solution.asteroidCollision([-2,5,10,-5,-3,1,3,-8])
print(answer)