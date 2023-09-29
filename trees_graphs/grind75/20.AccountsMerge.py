from collections import defaultdict
from typing import List

# https://leetcode.com/problems/accounts-merge/
# Tags: Disjount Set Union (DSU), Union Find
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: Not timed
    #
    # Use Union Find to union disjoint sets of email addresses together. Then map them back to new
    # representative accounts, sort them, and return the new set of accounts
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        
        def find(x):
            if x not in parent:
                parent[x] = x
            elif parent[x] == x:
                return x
        
            return find(parent[x])
        
        def union(x, y):
            parent[find(x)] = find(y)
            
        # Step 1: Map each email to a representative account (the first one it appears in)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email not in parent:
                    parent[email] = i
                union(i, parent[email])
                
        # Step 2: Aggregate emails under the same representative account
        email_to_accounts = defaultdict(set)
        for i, account in enumerate(accounts):
            for email in account[1:]:
                email_to_accounts[find(parent[email])].add(email)
                
        # Step 3: Build the result
        result = []
        for idx, emails in email_to_accounts.items():
            result.append([accounts[idx][0]] + sorted(emails))
            
        return result

        
solution = Solution()
answer = solution.accountsMerge([["John","john_newyork@mail.com","johnsmith@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])
answer = solution.accountsMerge([["David","David0@m.co","David1@m.co"],["David","David3@m.co","David4@m.co"],["David","David4@m.co","David5@m.co"],["David","David2@m.co","David3@m.co"],["David","David1@m.co","David2@m.co"]])
print(answer)

# Input:
# accounts = [
#   ["John","johnsmith@mail.com","john_newyork@mail.com"],
#   ["John","johnsmith@mail.com","john00@mail.com"],
#   ["Mary","mary@mail.com"],
#   ["John","johnnybravo@mail.com"]]

# Output:
# accounts = [
#   ["John","john00@mail.com","john_newyork@mail.com","johnsmith@mail.com"],
#   ["Mary","mary@mail.com"],
#   ["John","johnnybravo@mail.com"]]

# Input:
# accounts = [
# ["David","David0@m.co","David1@m.co"],
# ["David","David3@m.co","David4@m.co"],
# ["David","David4@m.co","David5@m.co"],
# ["David","David2@m.co","David3@m.co"],
# ["David","David1@m.co","David2@m.co"]]

# Output:
# accounts = [["David","David0@m.co","David1@m.co","David2@m.co","David3@m.co","David4@m.co","David5@m.co"]]