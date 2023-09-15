from typing import List

# https://leetcode.com/problems/longest-common-prefix/
# Tags: Lexicographic sort, vertical scanning
class Solution:

    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: 12:30
    #
    # We start by vertically looping through each string, starting
    # with the first letter. If they all match, then we add it to
    # our longest prefix, and move on. If at any point they don't match,
    # or one word reaches its max length, we return the longest prefix
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = len(strs[0])
        longest_prefix = ''
        i = 0
        while (i < l):
            curr_char = None
            matching_char = True
            for str in strs:
                if i > len(str) - 1:
                    return longest_prefix

                if curr_char is None:
                    curr_char = str[i]
                elif curr_char != str[i]:
                    matching_char = False

            if matching_char:
                longest_prefix += curr_char
            else:
                break

            i += 1

        return longest_prefix
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    # Time: Not timed
    def longestCommonPrefixUsingSort(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        # lexicographically sort the strings. After doing so, we know we
        # only need to use the first and last strings prefixes in our
        # analysis
        strs = sorted(strs)

        first = strs[0]
        last = strs[-1]

        l = min(len(first), len(last))
        longest_prefix = ''

        for i in range(0, l):
            if first[i] == last[i]:
                longest_prefix += first[i]
            else:
                return longest_prefix
            
        return longest_prefix





        
solution = Solution()
answer = solution.longestCommonPrefix2(['ab', 'a'])
answer = solution.longestCommonPrefix2(['flowersarecool', 'flow', 'flight'])
answer = solution.longestCommonPrefix(['ab', 'abda', 'abra'])
print(answer)