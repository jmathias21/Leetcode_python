
from typing import List
from collections import defaultdict, OrderedDict

# https://leetcode.com/problems/find-players-with-zero-or-one-losses/editorial/
# Tags: Hash Map
class Solution:
    
    # Runtime Complexity: O(n)
    # Space Complexity: O(n)
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        lossesDict = {}

        for match in matches:
            lossesDict.setdefault(match[0], 0)
            lossesDict.update({match[1]: lossesDict.get(match[1], 0) + 1})

        noLosses = []
        oneLosses = []

        for player, losses in lossesDict.items():
            if losses == 0:
                noLosses.append(player)
            elif losses == 1:
                oneLosses.append(player)

        return [sorted(noLosses), sorted(oneLosses)]


solution = Solution()
answer = solution.findWinners([[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]])
print(answer)

# Input: matches = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
# Output: [[1,2,10],[4,5,7,8]]
# Explanation:
# Players 1, 2, and 10 have not lost any matches.
# Players 4, 5, 7, and 8 each have lost one match.
# Players 3, 6, and 9 each have lost two matches.
# Thus, answer[0] = [1,2,10] and answer[1] = [4,5,7,8].