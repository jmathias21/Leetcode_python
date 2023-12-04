from typing import List

# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/
# Tags: Hash Map
# Time: 11:00
class SparseVector:

    def __init__(self, nums: List[int]):
        self.v1 = {}
        for i, num in enumerate(nums):
            if num != 0:
                self.v1[i] = num        

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        dot_product = 0
        for i, num in vec.v1.items():
            if i in self.v1:
                dot_product += num * self.v1[i]
        return dot_product

v1 = SparseVector([1,0,0,2,3])
v2 = SparseVector([0,3,0,4,0])
ans = v1.dotProduct(v2)