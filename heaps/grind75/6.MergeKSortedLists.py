import heapq
from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# https://leetcode.com/problems/merge-k-sorted-lists/
# Tags: Heap
class Solution:

    # Runtime Complexity: O(n log k)
    # Space Complexity: O(n)
    # Time: 41:00
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        answer = ListNode()
        curr = answer
        heap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        while heap:
            _, i, node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return answer.next

        
solution = Solution()
answer = solution.mergeKLists([ListNode(1, ListNode(4, ListNode(5))),ListNode(1, ListNode(3, ListNode(4))), ListNode(2, ListNode(6))])
print(answer)