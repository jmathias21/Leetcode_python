from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(4 ^ n)
    # Space Complexity: O()
    # Time: 8:00
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        result = []
        letter_num_map = {
            1: [],
            2: ['a','b','c'],
            3: ['d','e','f'],
            4: ['g','h','i'],
            5: ['j','k','l'],
            6: ['m','n','o'],
            7: ['p','q','r','s'],
            8: ['t','u','v'],
            9: ['w','x','y','z'],
        }

        def backtrack(curr, i):
            if i >= len(digits):
                result.append("".join(curr))
                return
            
            for letter in letter_num_map[int(digits[i])]:
                curr.append(letter)
                backtrack(curr, i + 1)
                curr.pop()

        backtrack([], 0)
        return result
            
            

        
solution = Solution()
answer = solution.letterCombinations("23")
print(answer)