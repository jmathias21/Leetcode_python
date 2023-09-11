
from typing import List

# https://leetcode.com/problems/longest-substring-without-repeating-characters/editorial/
# Tags: Hash Map
class Solution:
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(min(n, m)): m = alphabet. Upper bound is 26 characters, so could also list as O(1)
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        longest = 0
        mp = {}

        for j in range(len(s)):
            if s[j] in mp:
                i = max(mp[s[j]] + 1, i)

            mp[s[j]] = j

            longest = max(longest, (j - i) + 1)
            

        return longest

  

solution = Solution()
answer = solution.lengthOfLongestSubstring("abcabcbb")
print(answer)

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

# ij
# a b c a b c b b    longest = 1
# mp = {['a', 0]}

# i j
# a b c a b c b b    longest = 2
# mp = {['a', 0], ['b', 1]}

# i   j
# a b c a b c b b    longest = 3
# mp = {['a', 0], ['b', 1], ['c', 2]}

#   i   j
# a b c a b c b b    longest = 3
# mp = {['a', 0], ['b', 1], ['c', 2]}
# 'a' is in map, so i is moved to mp['a'] + 1 = 0 + 1 = 1
# mp = {['a', 3], ['b', 1], ['c', 2]}

#     i   j
# a b c a b c b b    longest = 3
# mp = {['a', 0], ['b', 1], ['c', 2]}
# 'b' is in map, so i is moved to mp['b'] + 1 = 1 + 1 = 2
# mp = {['a', 3], ['b', 4], ['c', 2]}

#       i   j
# a b c a b c b b    longest = 3
# mp = {['a', 3], ['b', 4], ['c', 2]}
# 'c' is in map, so i is moved to mp['c'] + 1 = 2 + 1 = 3
# mp = {['a', 3], ['b', 4], ['c', 5]}

#           i j
# a b c a b c b b    longest = 3
# mp = {['a', 3], ['b', 4], ['c', 5]}
# 'b' is in map, so i is moved to mp['b'] + 1 = 4 + 1 = 5
# mp = {['a', 3], ['b', 6], ['c', 5]}

#               ij
# a b c a b c b b    longest = 3
# mp = {['a', 3], ['b', 6], ['c', 5]}
# 'b' is in map, so i is moved to mp['b'] + 1 = 6 + 1 = 7
# mp = {['a', 3], ['b', 7], ['c', 5]}