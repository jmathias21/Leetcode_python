from typing import List

# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Tags: Backtracking, recursion, combinations
class Solution:

    # Runtime Complexity: O(4 ^ n)
    # Space Complexity: O()
    # Time: 18:00
    #
    # Use backtracking to recurse through every possible combination of letters for each digit.
    # Instead of concatenating strings throughout, we use an array to track letter combinations,
    # and we join them at the very end
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []

        num_letter_map = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z'],
        }

        answer = []

        def backtrack(curr, i):
            if len(curr) == len(digits):
                answer.append("".join(curr))
                return

            for letter in num_letter_map[digits[i]]:
                curr.append(letter)
                backtrack(curr, i + 1)
                curr.pop()

        backtrack([], 0)
        return answer


        
solution = Solution()
answer = solution.letterCombinations("23")
print(answer)