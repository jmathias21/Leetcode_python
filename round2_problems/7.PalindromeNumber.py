# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 1:02
    def isPalindrome(self, x: int) -> bool:
        if x == 0:
            return True

        # check if first digit is a negative sign
        if x < 0 or x % 10 == 0:
            return False

        reversed = 0
        i = 1
        # if not, parse all digits
        while x > reversed:
            reversed *= 10
            reversed += (x % 10)

            x //= 10

        return x == reversed or x == reversed // 10

            

        
solution = Solution()
answer = solution.isPalindrome(12321)
answer = solution.isPalindrome(11)
answer = solution.isPalindrome(1001001)
print(answer)