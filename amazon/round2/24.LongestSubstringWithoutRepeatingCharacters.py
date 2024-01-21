from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 2:34
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        left = 0
        longest = 0

        for i, char in enumerate(s):
            if char in char_map:
                left = max(left, char_map[char] + 1)
            char_map[char] = i
            longest = max(longest, i - left + 1)

        return longest

        
solution = Solution()
answer = solution.lengthOfLongestSubstring("abcabcbb")
print(answer)