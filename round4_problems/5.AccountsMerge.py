from collections import defaultdict
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 28:00
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}

        def find(x):
            if x not in parent:
                parent[x] = x
            elif parent[x] == x:
                return x
            
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x = find(x)
            root_y = find(y)
            parent[root_y] = root_x

        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email not in parent:
                    parent[email] = i
                else:
                    union(i, parent[email])

        grouped_accounts = defaultdict(set)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                grouped_accounts[find(email)].add(email)

        output = []
        for account in grouped_accounts.items():
            output.append([accounts[account[0]][0]] + sorted(account[1]))

        return output

        
solution = Solution()
# answer = solution.accountsMerge(
#     [["David","David0@m.co","David4@m.co","David3@m.co"],
#      ["David","David5@m.co","David5@m.co","David0@m.co"],
#      ["David","David1@m.co","David4@m.co","David0@m.co"],
#      ["David","David0@m.co","David1@m.co","David3@m.co"],
#      ["David","David4@m.co","David1@m.co","David3@m.co"]])
answer = solution.accountsMerge(
    [["John","johnsmith@mail.com","john_newyork@mail.com"],
     ["John","johnsmith@mail.com","john00@mail.com"],
     ["Mary","mary@mail.com"],
     ["John","johnnybravo@mail.com"]])
print(answer)

# [["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
# ["Mary","mary@mail.com"],
# ["John","johnnybravo@mail.com"]]


# [["David","David0@m.co","David4@m.co","David3@m.co"],
# ["David","David5@m.co","David5@m.co","David0@m.co"],
# ["David","David1@m.co","David4@m.co","David0@m.co"],
# ["David","David0@m.co","David1@m.co","David3@m.co"],
# ["David","David4@m.co","David1@m.co","David3@m.co"]]