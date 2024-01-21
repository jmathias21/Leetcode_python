from typing import List

class TrieNode:
    def __init__(self):
        self.is_terminal = False
        self.children = {}
        self.product_indices = []

# 
# Tags: 
class Solution:

    # Runtime Complexity: O(M) where M is the total number of chars in products
    # Space Complexity: O()
    # Time: started 2:46
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        head = TrieNode()

        # add words to trie
        for i, product in enumerate(products):
            curr = head
            for char in product:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr.children[char].product_indices.append(i)
                curr = curr.children[char]
            curr.is_terminal = True

        # search for them
        result = []
        def dfs(node: TrieNode, i: int):
            if len(result) < i:
                result.append([products[x] for x in node.product_indices[:3]])

            if i >= len(searchWord):
                return
            
            if searchWord[i] in node.children:
                dfs(node.children[searchWord[i]], i + 1)

        dfs(head, 0)
        result.extend([[]] * (len(searchWord) - len(result)))
        return result


        
solution = Solution()
answer = solution.suggestedProducts(products = ["havana"], searchWord = "tatiana")
answer = solution.suggestedProducts(products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse")
print(answer)