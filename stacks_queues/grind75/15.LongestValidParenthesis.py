# https://leetcode.com/problems/longest-valid-parentheses/
# Tags: Stack
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: Not timed
    #
    # When we see a left paren, push the index to the stack. When we see a right paren, pop the last element
    # in the stack and calculate the longest by subtracting the current index from the popped index
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        longest = 0

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    longest = max(longest, i - stack[-1])
                else:
                    stack.append(i)

        return longest

        
solution = Solution()
answer = solution.longestValidParentheses(")()())")
answer = solution.longestValidParentheses("()))()()") # 4
# 0, 
answer = solution.longestValidParentheses("()))((()))") # 6
answer = solution.longestValidParentheses("(())()(()((") # 6
answer = solution.longestValidParentheses("))))((()((") # 2
answer = solution.longestValidParentheses("))()((") # 2
print(answer)