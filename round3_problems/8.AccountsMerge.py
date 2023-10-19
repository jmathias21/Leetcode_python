from collections import defaultdict
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 11:08
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        rank = [0 for _ in range(len(accounts))]

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

            if root_x != root_y:
                if rank[root_x] < rank[root_y]:
                    parent[root_x] = root_y
                elif rank[root_y] < rank[root_x]:
                    parent[root_y] = root_x
                else:
                    parent[root_y] = root_x
                    parent[root_x] += 1

        for i, account in enumerate(accounts):
            parent[i] = i
            for j in range(1, len(account)):
                if account[j] not in parent:
                    parent[account[j]] = i
                union(i, account[j])

        new_accounts = defaultdict(set)
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                new_accounts[find(account[j])].add(account[j])

        answer = []
        for i, emails in new_accounts.items():
            answer.append([accounts[i][0]] + sorted(emails))

        return answer



        
solution = Solution()
answer = solution.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],
                                 ["John","johnsmith@mail.com","john00@mail.com"],
                                 ["Mary","mary@mail.com"],
                                 ["John","johnnybravo@mail.com"]])
print(answer)