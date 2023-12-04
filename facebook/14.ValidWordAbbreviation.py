# https://leetcode.com/problems/valid-word-abbreviation/
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: 14:00
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        curr_num = 0
        for char in abbr:
            if char.isdigit():
                if char == "0" and curr_num == 0:
                    return False
                curr_num *= 10
                curr_num += int(char)
            else:
                if curr_num > 0:
                    i += curr_num
                    curr_num = 0
                if i >= len(word) or word[i] != char:
                    return False
                i += 1

        if curr_num == 0 and i < len(word):
            return False

        return True if curr_num == 0 else curr_num == len(word) - i

        
solution = Solution()
answer = solution.validWordAbbreviation("ab", "a")
answer = solution.validWordAbbreviation("substitution", "s11")
print(answer)