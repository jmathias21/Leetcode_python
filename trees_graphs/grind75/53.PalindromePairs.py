from typing import List

# https://leetcode.com/problems/palindrome-pairs/
# Tags: Hash Map
class Solution:

    # Runtime Complexity: O(k^2 * n)
    # Space Complexity: O((k + n) ^ 2)
    # Time: Not timed
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def isPalindrome(str):
            return str == str[::-1]
        
        reverse_map = {}
        output = set()

        for i, word in enumerate(words):
            reverse_map[word[::-1]] = i

        for i, word in enumerate(words):
            # handle empty string case
            if "" in reverse_map and word != "" and isPalindrome(word):
                output.add((i, reverse_map[""]))
                output.add((reverse_map[""], i))

            # Iteratively split the word between prefix and suffix. If the prefix is in our map,
            # then we simply need to check if the suffix is a palindrome
            for j in range(len(word)):
                prefix, suffix = word[:j], word[j:]
                if prefix in reverse_map and isPalindrome(suffix) and i != reverse_map[prefix]:
                    output.add((i, reverse_map[prefix]))
                if suffix in reverse_map and isPalindrome(prefix) and i != reverse_map[suffix]:
                    output.add((reverse_map[suffix], i))

        return output

        
solution = Solution()
answer = solution.palindromePairs(["a","b","c","ab","ac","aa"])
answer = solution.palindromePairs(["b","ab"])
answer = solution.palindromePairs(["abcd","dcba","lls","s","sssll"])
print(answer)