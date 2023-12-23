from itertools import combinations
from typing import List
from collections import defaultdict

# https://leetcode.com/problems/analyze-user-website-visit-pattern/
# Tags: Hash Map, Combinations
class Solution:

    # Runtime Complexity: O(N choose 3) = O(N ^ 3)
    # Space Complexity: O(N)
    # Time: started 11:09
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        length = len(username)
        user_visits = defaultdict(list)
        score_map = defaultdict(int)
        highest_score = 0

        # store timestamped website visited for each user
        for i in range(length):
            user_visits[username[i]].append((timestamp[i], website[i]))

        for websites_visited in user_visits.values():
            if len(websites_visited) < 3:
                continue

            # sort the websites visited by their timestamp
            websites_visited.sort()

            # get all unique combinations of website patterns
            patterns = set(combinations([x[1] for x in websites_visited], 3))

            # record how many times we've seen each pattern
            for pattern in patterns:
                score_map[pattern] += 1
                highest_score = max(highest_score, score_map[pattern])

        # store the highest scored patterns in a list and then sort them lexicographically
        highest_score_patterns = []
        for pattern, score in score_map.items():
            if score == highest_score:
                highest_score_patterns.append(pattern)
        most_visited_pattern = sorted(highest_score_patterns)[0]
        return [most_visited_pattern[0], most_visited_pattern[1], most_visited_pattern[2]]




        
solution = Solution()
answer = solution.mostVisitedPattern(username = ["h","eiy","cq","h","cq","txldsscx","cq","txldsscx","h","cq","cq"], timestamp = [527896567,334462937,517687281,134127993,859112386,159548699,51100299,444082139,926837079,317455832,411747930], website = ["hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","yljmntrclw","hibympufi","yljmntrclw"])
answer = solution.mostVisitedPattern(["ua","ua","ua","ub","ub","ub"], timestamp = [1,2,3,4,5,6], website = ["a","b","a","a","b","c"])
answer = solution.mostVisitedPattern(["dowg","dowg","dowg"], [158931262,562600350,148438945], ["y","loedo","y"])
answer = solution.mostVisitedPattern(["joe","joe","joe","james","james","james","james","mary","mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"])
print(answer)