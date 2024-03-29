# https://leetcode.com/problems/valid-word-abbreviation/
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: 14:00
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        num = 0
        for char in abbr:
            if char.isdigit():
                if char == '0' and num == 0:
                    return False
                num = num * 10 + int(char)
            else:
                i += num
                num = 0

                if i >= len(word) or word[i] != char:
                    return False
                i += 1

        return i + num == len(word)

        
solution = Solution()
answer = solution.validWordAbbreviation("ab", "a")
answer = solution.validWordAbbreviation("substitution", "s11")
print(answer)