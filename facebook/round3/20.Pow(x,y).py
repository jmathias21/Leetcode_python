from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(logn)
    # Space Complexity: O()
    # Time: started 3:30
    def myPow(self, x: float, n: int) -> float:
        result = 1

        if n < 0:
            n = -n
            x = 1.0 / x

        while n > 0:
            if n % 2 == 0:
                n /= 2
                x *= x
            else:
                n -= 1
                result *= x

        return result


        
solution = Solution()
answer = solution.myPow(2, 5)
print(answer)