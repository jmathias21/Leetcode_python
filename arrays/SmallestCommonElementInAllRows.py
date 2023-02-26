from typing import List

# https://leetcode.com/problems/find-smallest-common-element-in-all-rows/description/
class Solution:
    
    # Runtime Complexity: O(mn)
    # Space Complexity: O(n)
    #
    # This solution tracks pointers to the indices in each row and
    # iteratively moves the pointers up until all rows match on the
    # smallest common element, or a pointer is moved to an index that
    # is higher, in which case all other pointers now increment
    # their indices in an attempt to match:
    #
    # [1,2,3,4,5]
    #  ^  <-- Pointer
    # [2,4,5,8,10]
    #  ^
    # [3,5,7,9,11]
    #  ^
    # [1,3,5,7,9]
    #  ^
    def rowPositions(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        least = -1
        pointers = [0] * m
        matching = 0

        while True:
            for x in range(m):
                if matching == m:
                    return least
                while True:
                    val = mat[x][pointers[x]]
                    if val == least:
                        matching += 1
                        break
                    elif val > least:
                        matching = 1
                        least = val
                        break
                    else:
                        if pointers[x] >= n - 1:
                            return -1
                        else:
                            pointers[x] += 1

            
solution = Solution()
answer = solution.rowPositions([[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]])
print(answer)