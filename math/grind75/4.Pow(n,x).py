# https://leetcode.com/problems/powx-n/
# Tags: Binary Exponentiation, Math
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 2:58
    def myPow(self, x: float, n: int) -> float:
        return self.binaryExp(x, n)

    def binaryExp(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        elif n < 0:
            n *= -1
            x = 1.0 / x
        
        result = 1
        
        while n != 0:
            if n % 2 == 0:
                x *= x
                n //= 2
            else:
                result *= x
                n -= 1

        return result
        

        
solution = Solution()
answer = solution.myPow(2, 100)
answer = solution.myPow(3, 3)
print(answer)