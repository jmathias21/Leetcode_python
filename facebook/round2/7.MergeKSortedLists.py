from typing import Optional, List
import heapq

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# https://leetcode.com/problems/merge-k-sorted-lists/
# Tags: 
class Solution:

    # Runtime Complexity: O(n logk)
    # Space Complexity: O(n)
    # Time: started 8:40
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy
        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        while heap:
            _, i, node = heapq.heappop(heap)
            head.next = node
            head = head.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next

        
solution = Solution()
answer = solution.mergeKLists([ListNode(1, ListNode(4, ListNode(5))), ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))])
print(answer)

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted list:
# 1->1->2->3->4->4->5->6