from typing import List

# 
# Tags: 
# Time: started 3:00
class SparseVector:

    def __init__(self, nums: List[int]):
        self.vector = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.vector[i] = num


    # Return the dotProduct of two sparse vectors
    # Runtime Complexity: O(n)
    def dotProduct(self, vec: 'SparseVector') -> int:
        product = 0
        for i, num in self.vector.items():
            if i in vec.vector:
                product += num * vec.vector[i]

        return product


v1 = SparseVector([1,0,0,2,3])
v2 = SparseVector([0,3,0,4,0])
ans = v1.dotProduct(v2)