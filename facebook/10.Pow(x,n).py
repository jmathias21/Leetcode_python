 # Tags: Math
class Solution:

    # Runtime Complexity: O(log n)
    # Space Complexity: O(1)
    # Time: started 10:49
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            n = -n
            x = 1.0 / x

        result = 1

        while n != 0:
            if n % 2 == 0:
                n /= 2
                x *= x
            else:
                n -= 1
                result *= x

        return result
        
solution = Solution()
answer = solution.myPow(2, 10)
print(answer)

# Input: x = 2.00000, n = 10
# Output: 1024.00000