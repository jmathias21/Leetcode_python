from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 8:11
    def countAndSay(self, n: int) -> str:
        digit_str = ["1"]

        for _ in range(n - 1):
            numbers = [(digit_str[0], 0)]
            for i in range(len(digit_str)):
                if digit_str[i] == numbers[-1][0]:
                    numbers[-1] = (numbers[-1][0], numbers[-1][1] + 1)
                else:
                    numbers.append((digit_str[i], 1))
            
            # create new digit string
            digit_str = []
            for number, count in numbers:
                digit_str.append(str(count))
                digit_str.append(number)

        return "".join(digit_str)

        
solution = Solution()
answer = solution.countAndSay(4)
print(answer)