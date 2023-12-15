from typing import List

# https://leetcode.com/problems/asteroid-collision/
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 8:00
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and stack[-1] > 0:
                    if stack[-1] > abs(asteroid):
                        break
                    elif stack[-1] < abs(asteroid):
                        stack.pop()
                    else:
                        stack.pop()
                        break
                else:
                    stack.append(asteroid)

        return stack

solution = Solution()
answer = solution.asteroidCollision([5,10,-5])
answer = solution.asteroidCollision([-5,2,3,4,5,-8,10,-5])
print(answer)