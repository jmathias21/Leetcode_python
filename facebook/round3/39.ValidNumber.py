from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time:
    def isNumber(self, s: str) -> bool:
        if "inf" in s.lower() or s == "nan":
            return False

        try:
            float(s)
        except ValueError:
            return False
        return True

        
solution = Solution()
answer = solution.isNumber()
print(answer)