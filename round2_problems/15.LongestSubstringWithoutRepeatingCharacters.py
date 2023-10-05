# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 24:00
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        longest = 0
        current = 0
        left = 0

        for i in range(len(s)):
            if s[i] not in char_map:
                char_map[s[i]] = i
                current += 1
            else:
                left = max(left, char_map[s[i]] + 1)
                current = (i - left) + 1
                char_map[s[i]] = i

            longest = max(longest, current)

        return longest

        
solution = Solution()
#answer = solution.lengthOfLongestSubstring("tmmzuxt")
#answer = solution.lengthOfLongestSubstring(" ")
#answer = solution.lengthOfLongestSubstring("pwwkew")
answer = solution.lengthOfLongestSubstring("abcabcbb")
print(answer)