from collections import defaultdict

# https://leetcode.com/problems/longest-palindrome/
# Tags: Hash map
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(1)
    # Time: 26:00
    def longestPalindrome(self, s: str) -> int:
        d = defaultdict(int)
        total = 0
        contains_single = False

        for c in s:
            # count number of each letter in string and store
            # in hashmap
            d[c] += 1

        for char_count in d.values():
            # divide the character count by 2 so that we can tally up
            # the doubles that we see. A double counts for 2 because it
            # can represent the left and right side in a palindrome
            x = char_count / 2
            total += int(x) * 2

            # A palindrome can only have one single count character, which
            # goes in the very middle of the palindrome. e.g. in "aabaa"
            # the "b" is the single character. Therefore if we find any singles
            # we increase the total count by a maximum of 1, but only one time 
            if (not contains_single):
                contains_single = not x.is_integer()

        return int(total + contains_single)
        
solution = Solution()
answer = solution.longestPalindrome("ccc") #ccc, total = 3
answer = solution.longestPalindrome("abccccdd") #dccaccd, total = 7
print(answer)