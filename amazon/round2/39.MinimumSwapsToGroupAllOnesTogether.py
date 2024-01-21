from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
# Tags: 
class Solution:

    # Runtime Complexity: O()
    # Space Complexity: O()
    # Time: 
    def minSwaps(self, data: List[int]) -> int:
        total_ones = sum(data)
        window_ones = 0
        max_window = 0

        for i in range(len(data)):
            if data[i] == 1:
                window_ones += 1
                print(True)
            if i > total_ones:
                # print(data[i - total_ones])
                if data[i - total_ones] == 1:
                    window_ones -= 1
            max_window = max(max_window, window_ones)
            print(max_window)

        # print(total_ones)
        # print(max_window)
        return total_ones - max_window
        

        
solution = Solution()
answer = solution.minSwaps([0,0,0,1,0])
print(answer)