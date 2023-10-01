from typing import List

class TrieNode:
    def __init__(self):
        self.is_terminal = False
        self.children = {}

# https://leetcode.com/problems/word-break/
# Tags: 
class Solution:
    
    # Runtime Complexity: O(n * m * k) where n is length of s, m = is length of longest word, and k is word count
    # Space Complexity: O(n)
    # Time: Not timed
    #
    # Uses dynamic programming to build up the solution, starting with the smallest
    # substring of s and then increasing its size. The dp array tracks whether substrings
    # can be segmented by wordDict, where the index of the dp value equals the substring
    # length
    def wordBreakUsingDP(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for word in wordDict:
                if i >= len(word) and dp[i - len(word)] and s[i - len(word):i] == word:
                    dp[i] = True
                    break

        return dp[n]

    # Runtime Complexity: O((n ^ 2) + (m * k)) - see comments for details
    # Space Complexity: O(n + (m * k)) - n space for dp array, plus space for prefix tree
    # Time: Not timed
    #
    # This solution uses a prefix tree and dynamic programming. We loop through s and build up
    # substrings to check against the wordDict. The prefix tree is used to speed up checks to see
    # if the current substring is in WordDict. The dp array is used to keep track of substrings
    # that have been determined to be segmentable, and then used to increase the efficiency by
    # ignoring substrings that aren't valid
    def wordBreakUsingDPAndTrie(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)

        root = TrieNode()

        # build prefix tree from wordDict. Time complexity is O(M * K) because
        # we need to iterate over all characters in all words. So M = the max length
        # of all words, and K = the total words
        for word in wordDict:
            node = root
            for i, c in enumerate(word):
                if c not in node.children:
                    node.children[c] = TrieNode()

                node = node.children[c]
                if i == len(word) - 1:
                    node.is_terminal = True

        # create a dp array that stores True if a substring of s, from 0
        # to the index in the array, can be segmented by the wordDict. e.g.
        # s = "leet" and wordDict = ["leet","code"] would be segmentable, so
        # we store dp[3] = True (because dp[3] represents the substring "leet").
        dp = [False] * n

        # This loop scans through each character in the string 's'. Starting from each character 'i', 
        # it tries to find valid words from the dictionary by navigating through the Trie data structure ('root'). 
        # If a valid word is found in the Trie that ends at position 'j', it marks 'dp[j]' as True. 
        # The check at 'i == 0 or dp[i - 1]' ensures it only tries to form words when 'i' is at the start or 
        # if there's a valid word that ends just before 'i' by checking the dp array, ensuring continuous
        # word segmentation without gaps.
        # Time complexity is O(N ^ 2) because of the nested for loop
        for i in range(n):
            if i == 0 or dp[i - 1]:
                curr = root
                for j in range(i, n):
                    c = s[j]
                    if c not in curr.children:
                        # No words exist
                        break

                    curr = curr.children[c]
                    if curr.is_terminal:
                        dp[j] = True

        return dp[-1]
        
        
solution = Solution()
answer = solution.wordBreakUsingDP("leetcodeleet", ["leet","code"])
answer = solution.wordBreakUsingDP("a", ["aa","aaa","aaaa","aaaaa","aaaaaa"])
answer = solution.wordBreakUsingDP("bb", ["a","b","bbb","bbbb"])
answer = solution.wordBreakUsingDP("catsandog", ["cat","sand","dog"])
answer = solution.wordBreakUsingDP("catsandog", ["cats","dog","sand","and","cat"])
answer = solution.wordBreakUsingDP("aaaaaaa", ["aaaa","aaa"])
answer = solution.wordBreakUsingDP("aaaaaaa", ["aaaa","aa"])
print(answer)


