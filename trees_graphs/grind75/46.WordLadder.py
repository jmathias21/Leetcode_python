from collections import defaultdict, deque
from typing import List

# https://leetcode.com/problems/word-ladder/
# Tags: BFS, Graph, Hash Map
class Solution:

    # Runtime Complexity: O(M^2 * N) where M is the max length of each word, and N is the wordList
    # Space Complexity: O(M^2 * N)
    # Time: started 1:34
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        d = defaultdict(set)

        for word in wordList:
            for i in range(len(word)):
                interm = word[:i] + '*' + word[i + 1:]
                d[interm].add(word)

        seen = set([beginWord])
        queue = deque([(beginWord, 1)])
        while queue:
            word, depth = queue.popleft()

            for i in range(len(word)):
                interm = word[:i] + '*' + word[i + 1:]
                for w in d[interm]:
                    if w == endWord:
                        return depth + 1
                    if w not in seen:
                        seen.add(w)
                        queue.append((w, depth + 1))
                d[interm] = set()

        return 0

        
solution = Solution()
answer = solution.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"])
print(answer)