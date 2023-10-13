from typing import List

# https://leetcode.com/problems/daily-temperatures/
# Tags: Monotonic decreasing stack
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: Not timed
    #
    # Loop through temperatures, adding each temperature index to a stack at each step. If the current day's temp
    # is heigher than the temp on top of the stack, pop it off the stack and add the difference in days to our
    # answer array. Continue popping off the stack for the current day until the current day's temp is smaller or
    # equal to the top of the stack, and move onto the next day
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)

        for curr_day, curr_temp in enumerate(temperatures):
            while stack and curr_temp > temperatures[stack[-1]]:
                prev_day = stack.pop()
                answer[prev_day] = curr_day - prev_day

            stack.append(curr_day)

        return answer

        
solution = Solution()
answer = solution.dailyTemperatures([73,74,75,71,69,72,76,73])
print(answer)

# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]

# [73,74,75,71,69,72,76,73]
#  ^
# add 73, s = [73]
# answer = [0, 0, 0, 0, 0, 0, 0, 0]

# [73,74,75,71,69,72,76,73]
#     ^
# 74 > 73, pop 73
# add 74, s = [74]
# answer = [1, 0, 0, 0, 0, 0, 0, 0]

# [73,74,75,71,69,72,76,73]
#        ^
# 75 > 74, pop 74
# add 75, s = [75]
# answer = [1, 1, 0, 0, 0, 0, 0, 0]

# [73,74,75,71,69,72,76,73]
#           ^
# 71 < 74, do nothing
# add 71, s = [75, 71]
# answer = [1, 1, 0, 0, 0, 0, 0, 0]

# [73,74,75,71,69,72,76,73]
#              ^
# 69 < 71, do nothing
# add 69, s = [75, 71, 69]
# answer = [1, 1, 0, 0, 0, 0, 0, 0]

# [73,74,75,71,69,72,76,73]
#                 ^
# 72 > 69, pop 69
# s = [75, 71]
# 72 > 71, pop 71
# s = [75]
# add 72, s = [75, 72]
# answer = [1, 1, 0, 2, 1, 0, 0, 0]

# [73,74,75,71,69,72,76,73]
#                    ^
# 76 > 72, pop 72
# s = [75]
# 76 > 75, pop 75
# s = []
# add 76, s = [76]
# answer = [1, 1, 4, 2, 1, 1, 0, 0]

# [73,74,75,71,69,72,76,73]
#                       ^
# 73 < 72, do nothing
# add 73, s = [76, 73]
# answer = [1, 1, 4, 2, 1, 1, 0, 0]