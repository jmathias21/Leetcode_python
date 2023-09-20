# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Tags: sliding window, Hash Map
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 41:00
    #
    # Uses a sliding window and a hashmap that tracks indexes of characters
    # seen. If we see a character that's been used, we move the left side of
    # the window to the last seen index + 1. Every new character seen, we
    # determine if the current sliding window substring is the longest
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0

        # tracks indexes of characters that have been seen
        chars_used = {}

        # tracks the maximum substring seen
        max_length = 0

        for i in range(len(s)):
            if s[i] in chars_used:
                left = max(left, chars_used.get(s[i]) + 1)

            chars_used[s[i]] = i

            max_length = max(max_length, len(s[left:i + 1]))

        return max_length

            
        
solution = Solution()
answer = solution.lengthOfLongestSubstring("pwwkew")
answer = solution.lengthOfLongestSubstring("abcabcbb")
answer = solution.lengthOfLongestSubstring("tmmzuxt")
answer = solution.lengthOfLongestSubstring("ynyo")
answer = solution.lengthOfLongestSubstring("dvdf")
print(answer)


# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

# Example: pwwkew
# chars_used = {}, left = 0, i = 0, curr_substr = [], max_length = 0
# chars_used = {'p': 0}, left = 0, i = 0, curr_substr = ['p'], max_length = 1
# chars_used = {'p': 0, 'w': 1}, left = 0, i = 1, curr_substr = ['p','w'], max_length = 2
# chars_used = {'p': 0, 'w': 2}, left = 2, i = 2, curr_substr = ['w'], max_length = 2
# chars_used = {'p': 0, 'w': 2, 'k': 3}, left = 2, i = 3, curr_substr = ['w','k'], max_length = 2
# chars_used = {'p': 0, 'w': 2, 'k': 3, 'e': 4}, left = 2, i = 4, curr_substr = ['w','k','e'], max_length = 3
# chars_used = {'p': 0, 'w': 5, 'k': 3, 'e': 4}, left = 3, i = 5, curr_substr = ['w'], max_length = 3