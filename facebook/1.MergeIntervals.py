from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n logn)
    # Space Complexity: O(n)
    # Time: 10:00
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] <= output[-1][1]:
                output[-1][1] = max(output[-1][1], intervals[i][1])
            else:
                output.append(intervals[i])

        return output


        
solution = Solution()
answer = solution.merge([[1,3],[2,6],[8,10],[15,18]])
print(answer)