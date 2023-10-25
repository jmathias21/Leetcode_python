from typing import List

# https://leetcode.com/problems/asteroid-collision/editorial/
# Tags: Stack
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: started 2:10
    #
    # As we iterate through the asteroid array, add asteroids to our stack. If we see a collision, we remove asteroids
    # from our stack depending on the results of the collision
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]

        for i in range(1, len(asteroids)):
            if asteroids[i] < 0:
                # as long as the stack has asteroids on a collision trajectory with
                # our current asteroid, remove them
                while stack and stack[-1] > 0 and stack[-1] < abs(asteroids[i]):
                    stack.pop()

                # if the stack is empty or the top element is negative, we can add our
                # asteroid onto it
                if len(stack) == 0 or stack[-1] < 0:
                    stack.append(asteroids[i])
                # if the asteroids are equal, blow them both up
                elif abs(stack[-1]) == abs(asteroids[i]):
                    stack.pop()
            else:
                stack.append(asteroids[i])

        return stack


        
solution = Solution()
answer = solution.asteroidCollision([-2,1,-2,-2])
answer = solution.asteroidCollision([5,10,-5,2,-2,3,4,-7])
answer = solution.asteroidCollision([5,10,-5])
print(answer)