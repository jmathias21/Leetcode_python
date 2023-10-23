from collections import defaultdict

# https://leetcode.com/problems/longest-repeating-character-replacement/
# Tags: Sliding window
class Solution:

    # Runtime Complexity: O(N)
    # Space Complexity: O(N)
    # Time: Not timed
    #
    # Create a dict that will represent the frequency of each char. Use a sliding window,
    # where both left and right start at index 0 and the right pointer slides to the right.
    # At each iteration, we update the frequency of the current character and find the new
    # maximum frequency we've seen so far. If the window size minus the max frequency is within
    # k, then we can store our new longest substring count. Otherwise, we increment our left
    # pointer
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = defaultdict(int)
        max_frequency = 0
        longest_substr = 0
        left = 0
        right = 0

        while right < len(s):
            frequency[s[right]] += 1
            max_frequency = max(max_frequency, frequency[s[right]])

            if right - left - max_frequency < k:
                longest_substr = max(longest_substr, (right - left) + 1)
            else:
                frequency[s[left]] -= 1
                left += 1
            right += 1

        return longest_substr
        

        
solution = Solution()
answer = solution.characterReplacement("CAAABCBABBA", 2) # 6
answer = solution.characterReplacement("AABABBA", 1) # 4
print(answer)