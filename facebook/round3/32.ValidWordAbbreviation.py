from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: started 11:30
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
answer = solution.validWordAbbreviation(word = "hi", abbr = "1")
answer = solution.validWordAbbreviation(word = "hi", abbr = "2i")
answer = solution.validWordAbbreviation(word = "a", abbr = "2")
answer = solution.validWordAbbreviation(word = "internationalization", abbr = "i5a11o1")
answer = solution.validWordAbbreviation(word = "internationalization", abbr = "i12iz4n")
print(answer)