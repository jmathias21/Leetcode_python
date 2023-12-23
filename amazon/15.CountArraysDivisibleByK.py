from typing import List
from collections import Counter, defaultdict
import math

# https://leetcode.com/problems/count-array-pairs-divisible-by-k/
# Tags: 
class Solution:

    # Runtime Complexity: O(n^2)
    # Space Complexity: O(n)
    # Time: started 5:50
    def countPairs(self, nums, k):
        gcd_counter = Counter()
        ans = 0
        
        for num in nums:
            gcd_value = math.gcd(k, num)  # Find GCD of k and current number
            complement_factor = k // gcd_value  # Compute the complement factor
            
            # Check if any number in counter is a multiple of 'complement_factor'
            for key in gcd_counter:
                if key % complement_factor == 0:
                    ans += gcd_counter[key]  # Increment answer by the frequency of the found number
            
            # Increase the frequency of the GCD value
            gcd_counter[gcd_value] += 1
        
        return ans

        
solution = Solution()
answer = solution.countPairs([1,2,3,4,5], 2)
print(answer)