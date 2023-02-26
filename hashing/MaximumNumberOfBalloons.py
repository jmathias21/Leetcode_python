
from typing import List
from collections import defaultdict

# https://leetcode.com/problems/maximum-number-of-balloons/editorial/
# Tags: 
class Solution:
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    def maxNumberOfBalloons(self, text: str) -> int:
        n = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}

        for letter in text:
            if letter in n:
                if letter == "l" or letter == "o":
                    n[letter] += 0.5
                else:
                    n[letter] += 1

        return (int(min(n.values())))

    # Runtime Complexity: O(n + m) where n = text and m = pattern
    # Space Complexity: O(m)
    def maxNumberOfPattern(self, text: str, pattern: str) -> int:
        n = {}
        dupes = set()
        for letter in pattern:
            if (n.get(letter) == None):
                n[letter] = 0
            else:
                dupes.add(letter)

        for letter in text:
            if letter in n:
                if letter in dupes:
                    n[letter] += 0.5
                else:
                    n[letter] += 1

        return (int(min(n.values())))

        
            
solution = Solution()
answer = solution.maxNumberOfPattern("xloonbalxballpoon", "balloon")
print(answer)

# Input: text = "loonbalxballpoon"
# Output: 2