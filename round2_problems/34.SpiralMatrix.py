from typing import List

# Tags: 
class Solution:

    # Runtime Complexity: O(n * m)
    # Space Complexity: O(n * m)
    # Time: started 9:55
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        answer = []
        x, y = 0, 0
        curr_dir = 0
        visited = set()
        width = len(matrix[0])
        height = len(matrix)
        total_elements = width * height
        count = 0

        while count < total_elements:
            if (x, y) not in visited:
                count += 1
                visited.add((x, y))
                answer.append(matrix[y][x])

            if curr_dir == 0:
                if x >= width - 1 or (x + 1, y) in visited:
                    curr_dir = 1
                else:
                    x += 1
            elif curr_dir == 1:
                if y >= height - 1 or (x, y + 1) in visited:
                    curr_dir = 2
                else:
                    y += 1
            elif curr_dir == 2:
                if x <= 0 or (x - 1, y) in visited:
                    curr_dir = 3
                else:
                    x -= 1
            elif curr_dir == 3:
                if y <= 0 or (x, y - 1) in visited:
                    curr_dir = 0
                else:
                    y -= 1

        return answer
            


        
solution = Solution()
answer = solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
print(answer)