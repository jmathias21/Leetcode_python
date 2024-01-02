from collections import defaultdict
from typing import List

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(N * K * log(N * k))
    # Space Complexity: O()
    # Time: startedb 1:57
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}

        def find(x):
            if parent[x] == x:
                return x
            
            parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            parent[find(x)] = find(y)
        
        # union emails
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if i not in parent:
                    parent[i] = i
                if email not in parent:
                    parent[email] = i
                union(i, parent[email])

        # assign emails back to accounts
        emails_to_accounts = defaultdict(set)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                emails_to_accounts[find(parent[email])].add(email)    
        
        # build output
        result = []
        for i, account in emails_to_accounts.items():
            result.append([accounts[i][0]])
            for email in sorted(account):
                result[-1].append(email)

        return result

        
solution = Solution()
answer = solution.accountsMerge([["John","john_newyork@mail.com","johnsmith@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])
print(answer)