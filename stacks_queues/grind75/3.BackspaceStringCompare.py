# https://leetcode.com/problems/backspace-string-compare/
# Tags: stack
class Solution:

    # Runtime Complexity: O(m + n)
    # Space Complexity: O(m + n)
    # Time: 12:00
    #
    # Uses two stacks to keep track of the strings. When we see
    # a '#', we pop an element off the top. At the end, we compare
    # the two stacks
    def backspaceCompareUsingStack(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []

        for i in range(len(s)):
            if s[i] == '#':
                if s_stack:
                    s_stack.pop()
            else:
                s_stack.append(s[i])

        for i in range(len(t)):
            if t[i] == '#':
                if t_stack:
                    t_stack.pop()
            else:
                t_stack.append(t[i])

        return s_stack == t_stack
        
solution = Solution()
#answer = solution.backspaceCompareUsingReverseLoop('a##c', '#a#c')
answer = solution.backspaceCompareUsingReverseLoop('ab#c', 'ad#c')
print(answer)