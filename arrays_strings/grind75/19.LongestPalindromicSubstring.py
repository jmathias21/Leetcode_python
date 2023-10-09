from typing import List

# https://leetcode.com/problems/longest-palindromic-substring
# Tags: Palindromes
class Solution:

    # Runtime Complexity: O(n^2)
    # Space Complexity: O(n)
    # Time: Not timed
    #
    # Build up a stack of single and double character palindromes, then process them off of the
    # stack. As we process them, we check to see if the left and right characters of the current
    # palindrome are equal. If so, we can expand the palindrome and add it back to the stack.
    # We keep track of the longest palindrome throughout and return it at the end
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        stack = []
        longest = s[0]
        longest_size = 0
        
        # add the left and right indices for single and double character palindromes to our stack
        for i in range(length):
            stack.append((i, i))
            if i > 0 and s[i - 1] == s[i]:
                stack.append((i - 1, i))
                longest = s[i - 1:i + 1]
                longest_size = 1

        while stack:
            left, right = stack.pop()
            left -= 1
            right += 1

            if left < 0 or right >= length:
                continue

            # if we can expand our palindrome, add it back onto the stack and store our longest
            # palindrome
            if s[left] == s[right]:
                stack.append((left, right))
                palindrome = s[left:right + 1]
                if right - left > longest_size:
                    longest = palindrome
                    longest_size = right - left

        return longest

        
solution = Solution()
answer = solution.longestPalindrome("aaaaa")
answer = solution.longestPalindrome("cbbd")
answer = solution.longestPalindrome2("babad")
answer = solution.longestPalindrome("racecar")
print(answer)