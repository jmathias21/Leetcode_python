# https://leetcode.com/problems/add-binary/
# Tags: binary, binary conversion
class Solution:

    # Runtime Complexity: O(1)
    # Space Complexity: O(1)
    # Time: 4:00
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

        
solution = Solution()
answer = solution.addBinary("11", "1") # 100
print(answer)