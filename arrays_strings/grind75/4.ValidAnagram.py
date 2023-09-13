from collections import defaultdict

# https://leetcode.com/problems/valid-anagram/
# Tags: hashing, hashmap
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # this allows us to default values to 0
        d = defaultdict(int)
        
        for c in s:
            d[c] += 1

        for c in t:
            d[c] -= 1

        for val in d.values():
            if val != 0:
                return False
            
        return True

        
solution = Solution()
answer = solution.isAnagram("rat", "car") # valid
answer = solution.isAnagram("anagram", "nagaram") # invalid
print(answer)