from collections import deque
from typing import List

# https://leetcode.com/problems/01-matrix/
# Tags: BFS, matrix, graph, dynamic programming
class Solution:

    # Runtime Complexity: O(m * n)
    # Space Complexity: O(m * n)
    # Time: Not timed
    #
    # Solution:
    # 1. Create a copy of mat, we'll call it matrix.
    # 2. Use a data structure "seen" to mark nodes we have already visited and a queue for the BFS.
    # 3. Put all nodes with 0 into the queue. We will also track the level/number of steps with each queue entry. Mark these nodes in seen as well.
    # 4. Perform the BFS:
    #   1. While queue is not empty, get the current row, col, steps from the queue.
    #   2. Iterate over the 4 directions. For each nextRow, nextCol, check if it is in bounds and not already visited in seen.
    #   3. If so, set matrix[nextRow][nextCol] = steps + 1 and push nextRow, nextCol, steps + 1 onto the queue. Also mark nextRow, nextCol in seen.
    # 5. Return matrix.
    def updateMatrixUsingBFS(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        # deep copy the matrix to a new var
        matrix = [row[:] for row in mat]
        
        # use hashset to keep track of elements we've already seen
        seen = set()

        # use a queue to process nodes in the correct order (BFS)
        queue = deque()

        # find all 0's, add them as seen, and add them to queue
        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    seen.add((row, col))
                    queue.append((row, col, 0))

        while (queue):
            row, col, dis = queue.popleft()

            for d_row, d_col in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                n_row = d_row + row
                n_col = d_col + col

                # verify direction is within bounds and not yet seen
                if (n_row >= 0 and n_row < m 
                    and n_col >= 0 and n_col < n
                    and (n_row, n_col) not in seen):

                    # add element as seen
                    seen.add((n_row, n_col))

                    # calculate distance of this element based on the distance
                    # of the popped element. It should always be +1
                    matrix[n_row][n_col] = dis + 1

                    # add this element to the queue so we can begin processing
                    # its neighbors as well
                    queue.append((n_row, n_col, dis + 1))

        return matrix
    
    # Runtime Complexity: O(m * n)
    # Space Complexity: O(m * n)
    # Time: Not timed
    #
    # We know that the minimum of any dp[x][y] is equal to the minimum of the 4
    # surrounding elements + 1. However, we can't calculate that without knowing
    # what those elements are, so where do we start? We know that if we start at the
    # top left, that dp[x][y] is always the minimum of the element to the left and the
    # element above it. So we can take an initial pass from the top-left to the bottom-right,
    # and along the way we can find as many minimums as possible. Then we loop from the
    # bottom-right to the top-left to finish setting all of our minimums
    def updateMatrixUsingDynamicProgramming(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        # copy matrix into new matrix with large values
        dp = [[float('inf')] * n for _ in mat]

        # loop over original matrix and traverse down and to the right
        for row in range(m):
            for col in range(n):
                # if value is a 0, set new matrix to 0 at that spot
                if mat[row][col] == 0:
                    dp[row][col] = 0
                else:
                    if row > 0:
                        dp[row][col] = min(dp[row][col], dp[row - 1][col] + 1)
                    if col > 0:
                        dp[row][col] = min(dp[row][col], dp[row][col - 1] + 1)

        # loop over original matrix and traverse up and to the left
        for row in range(m - 1, -1, -1):
            for col in range(n - 1, -1, -1):
                if row < m - 1:
                    dp[row][col] = min(dp[row][col], dp[row + 1][col] + 1)
                if col < n - 1:
                    dp[row][col] = min(dp[row][col], dp[row][col + 1] + 1)

        return dp

        
        
solution = Solution()
answer = solution.updateMatrixUsingDynamicProgramming([[0,1,0,1,1],[1,1,0,0,1],[0,0,0,1,0],[1,0,1,1,1],[1,0,0,0,1]])
answer = solution.updateMatrixUsingDynamicProgramming([[0],[0],[0],[0],[0]])
answer = solution.updateMatrixUsingDynamicProgramming([[0,0,0],[0,1,0],[1,1,1]])
print(answer)

# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]

# [0,0,0]
# [0,1,0]
# [1,1,1]