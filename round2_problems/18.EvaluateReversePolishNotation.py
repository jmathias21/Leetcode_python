from typing import List

# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 17:00
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in ['+','-','/','*']:
                stack.append(token)
            else:
                right = int(stack.pop())
                left = int(stack.pop())
                total = 0

                if token == '+':
                    total = left + right
                elif token == '-':
                    total = left - right
                elif token == '/':
                    total = int(left / right)
                elif token == '*':
                    total = left * right

                stack.append(total)

        return int(stack[0])
                    

solution = Solution()
answer = solution.evalRPN(["4","13","5","/","+"])
answer = solution.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
answer = solution.evalRPN(["2","1","+","3","*"])
print(answer)