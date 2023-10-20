from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 4:24
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for _ in range(len(temperatures))]
        stack = []

        for i in range(len(temperatures)):
            while stack:
                idx, temp = stack[-1]
                if temperatures[i] > temp:
                    stack.pop()
                    answer[idx] = i - idx
                else:
                    break

            stack.append((i, temperatures[i]))
              

        return answer
                

        
solution = Solution()
answer = solution.dailyTemperatures([73,74,75,71,69,72,76,73])
print(answer)

# [1,1,4,2,1,1,0,0]