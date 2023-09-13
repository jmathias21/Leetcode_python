from collections import defaultdict

# https://leetcode.com/problems/ransom-note/
# Tags: hashmap
class Solution:
    # Runtime Complexity: 
    # Space Complexity: 
    # Time: 8:00
    #
    # Counts number of each character used in magazine string using a hashmap.
    # Then subtracts the amount ogf times each character used in the ransom note.
    # If we find that none of the characters in the hashmap were subtracted more
    # than they were added, then we know we can construct the ransom note from the
    # magazine
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if (len(magazine) < len(ransomNote)):
            return False

        d = defaultdict(int)

        for c in magazine:
            d[c] += 1

        for c in ransomNote:
            d[c] -= 1

        for x in d.values():
            if x < 0:
                return False
            
        return True
        
        
        
solution = Solution()
answer = solution.canConstruct("aab", "aabbc")
print(answer)