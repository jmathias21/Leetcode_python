from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 11:37
    def myPow(self, x: float, n: int) -> float:
        result = 1

        if n < 0:
            n *= -1
            x = 1.0 / x

        while n >= 1:
            if n % 2 == 0:
                x *= x
                n /= 2
            else:
                result *= x
                n -= 1

        return result


        
solution = Solution()
answer = solution.myPow(2, 100)
print(answer)

# (x ^ 2) ^ (n / 2) if n is even
# x * (x ^ 2) ^ ((n - 1) / 2) if n is odd to make it even