from collections import deque

# https://leetcode.com/problems/decode-string/
# Tags: Stack
class Solution:

    # Runtime Complexity: O(max(K) * N) where K is the highest digit number we see and N is the length of the string
    # Space Complexity: O(M + N) where M is the number of letters and N is the number of digits
    # Time: Not timed
    #
    # Iterate through the string, adding every character we see to a stack. When we see a closing bracket,
    # process elements off the stack until we see a number. Duplicate any characters we've seen by that number
    # and add it back onto the stack. Continue until we've iterated through all characters.
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
            else:
                curr = deque()
                digits = deque()
                while stack:
                    char = stack.pop()
                    if char.isalpha():
                        curr.appendleft(char)
                    elif char.isdigit():
                        digits.appendleft(char)
                        if not stack or not stack[-1].isdigit():
                            stack.extend(curr * int(''.join(digits)))
                            break

        return ''.join(stack)

        
solution = Solution()
answer = solution.decodeString("3[a2[c]2[b]]")
answer = solution.decodeString("100[leetcode]")
print(answer)