from collections import defaultdict
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 11:19
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        rank = defaultdict(int)

        def find(x):
            if parent[x] == x:
                return x
            
            return find(parent[x])
        
        def union(x, y):
            root_x = find(x)
            root_y = find(y)

            if rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            elif rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

        # union accounts
        # O(NK * a(n)) where N is max accounts, and K is max emails in account
        for i, account in enumerate(accounts):
            parent[i] = i
            for j in range(1, len(account)):
                if account[j] not in parent:
                    parent[account[j]] = i
                union(i, account[j])

        # build new account list
        # O(NK)
        new_accounts = defaultdict(set)
        for i, account in enumerate(accounts):
            for j in range(1, len(account)):
                new_accounts[find(account[j])].add(account[j])

        # finalize output
        # O(NK log N)
        answer = []
        for i, emails in new_accounts.items():
            answer.append([accounts[i][0]] + sorted(emails))

        return answer
        
        
solution = Solution()
answer = solution.accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])
print(answer)

# Input: accounts = [
#   ["John","johnsmith@mail.com","john_newyork@mail.com"],
#   ["John","johnsmith@mail.com","john00@mail.com"],
#   ["Mary","mary@mail.com"],
#   ["John","johnnybravo@mail.com"]]

# Output: [
#   ["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
#   ["Mary","mary@mail.com"],
#   ["John","johnnybravo@mail.com"]]