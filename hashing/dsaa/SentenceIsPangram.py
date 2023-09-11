from typing import List

# https://leetcode.com/problems/check-if-the-sentence-is-pangram/editorial/
# Tags: Hash Set
class Solution:
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    def checkIfPangram(self, sentence: str) -> bool:
        a = set()
        for s in sentence:
            a.add(s)

        return len(a) == 26

solution = Solution()
answer = solution.checkIfPangram("thequickbrownfoxjumpsoverthelazydog")
print(answer)

# Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
# Output: true
# Explanation: sentence contains at least one of every letter of the English alphabet.