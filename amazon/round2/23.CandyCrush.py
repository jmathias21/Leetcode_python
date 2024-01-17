from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 
    def candyCrush(self, s):
        stack = []

        for i, char in enumerate(s):
            if stack and stack[-1][0] == char:
                stack[-1] = (stack[-1][0], stack[-1][1] + 1)
                # check if next char is differet or we're at the end
                if i == len(s) - 1 or s[i + 1] != char:
                    if stack[-1][1] >= 3:
                        stack.pop()
            else:
                stack.append((char, 1))

        result = []
        for char, count in stack:
            result.extend([char] * count)

        return "".join(result)

        
solution = Solution()
answer = solution.candyCrush("aabbbaade")
answer = solution.candyCrush("aaabbbaaa")
answer = solution.candyCrush("aabbbaade")
answer = solution.candyCrush("aabbbaade")
answer = solution.candyCrush("abdefgdhaaa")
print(answer)