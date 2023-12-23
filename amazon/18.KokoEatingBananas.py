from typing import List
import math

# https://leetcode.com/problems/koko-eating-bananas/
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: started 11:10
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper_bound = max(piles)
        lower_bound = 1

        def hours_to_eat(k):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / k)
            return hours

        def search(left, right):
            mid = (left + right) // 2

            hours = hours_to_eat(mid)
            if left == right:
                return left

            if hours <= h:
                return search(left, mid)
            else:
                return search(mid + 1, right)
            
        return search(lower_bound, upper_bound)

        
solution = Solution()
# answer = solution.minEatingSpeed([3,6,7,11], 8) # 4
answer = solution.minEatingSpeed([30,11,23,4,20], 6) # 30
print(answer)