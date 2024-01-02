from typing import List

# https://leetcode.com/problems/pascals-triangle/
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 30:00
    def generate(self, numRows: int) -> List[List[int]]:
        output = []

        for i in range(numRows):
            row = [None for _ in range(i + 1)]
            row[0] = row[-1] = 1

            for j in range(1, len(row) - 1):
                row[j] = output[i - 1][j - 1] + output[i - 1][j]

            output.append(row)
        return output

        
solution = Solution()
answer = solution.generate(5)
print(answer)