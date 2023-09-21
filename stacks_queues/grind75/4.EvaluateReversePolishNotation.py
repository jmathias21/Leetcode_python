from typing import List
from collections import deque

# https://leetcode.com/problems/evaluate-reverse-polish-notation/editorial/
# Tags: reverse polish notation, stack, modify list in-place
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: Not timed
    #
    # Loop through the tokens and add numbers to a stack as we see them. When we
    # get to an operation token, pop the last two numbers and apply the operation.
    # Then add the total back onto the stack. Repeat until we have a single number
    # on our stack
    def evalRPNUsingStack(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token in '+-/*':
                n2 = stack.pop()
                n1 = stack.pop()

                if token == '+':
                    total = n1 + n2
                elif token == '-':
                    total = n1 - n2
                elif token == '*':
                    total = n1 * n2
                elif token == '/':
                    total = int(n1 / n2)

                stack.append(total)
            else:
                stack.append(int(token))

        return stack.pop()

    # Runtime Complexity: O(n^2) because deleting is O(n)
    # Space Complexity: O(1)
    # Time: Not timed
    #
    # Loop through the tokens. When we see an operation token, taken the previous two
    # numbers and apply the operation to them. Then update one of them with the total
    # and remove both the operation index and the other number index from the list.
    # Repeat until we arrive at our total
    def evalRPNUsingReduceListInPlace(self, tokens: List[str]) -> int:
        i = 0
        while len(tokens) > 1:
            if not tokens[i].lstrip('-').isnumeric():
                left_val = tokens[i - 2]
                right_val = tokens[i - 1]

                if tokens[i] == '+':
                    tokens[i - 2] = int(left_val) + int(right_val)
                elif tokens[i] == '-':
                    tokens[i - 2] = int(left_val) - int(right_val)
                elif tokens[i] == '*':
                    tokens[i - 2] = int(left_val) * int(right_val)
                elif tokens[i] == '/':
                    tokens[i - 2] = int(int(left_val) / int(right_val))
                
                del tokens[i]
                del tokens[i - 1]
                i -= 1
                continue

            i += 1

        return int(tokens[0])

        
solution = Solution()
answer = solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
answer = solution.evalRPNUsingStack(["4","13","5","/","+"])
answer = solution.evalRPN(["2","1","+","3","*"])
print(answer)

# Example for evalRPNUsingStack: ["4","13","5","/","+"]

# stack = []
# pop 4, stack = [4]
# pop 13, stack = [4, 13]
# pop 5, stack = [4, 13, 5]
# See "/", pop 5 then 13, then divide 13 / 5
# append 2, stack = [4, 2]
# See "+", pop 2 then 4, then add 4 + 2
# append 6, stack = [6]
# return 6