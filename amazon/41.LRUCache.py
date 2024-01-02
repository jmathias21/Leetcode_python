from typing import List

class ListNode:
    def __init__(self, key=-1, val=0, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

# https://leetcode.com/problems/lru-cache/
# Tags: 
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.d = {}

    def get(self, key: int) -> int:
        if key not in self.d:
            return -1

        # retrieve the node at key
        node = self.d[key]

        # move it to the end of the list as the MRU
        self.remove(node)
        node = ListNode(key, node.val)
        self.d[key] = node
        self.add(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.remove(self.d[key])

        node = ListNode(key, value)
        self.d[key] = node
        self.add(node)

        # check if over max size
        if len(self.d) > self.capacity:
            # remove LRU from list
            del self.d[self.head.next.key]
            self.remove(self.head.next)

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

obj = LRUCache(2)
obj.put("2", 1)
obj.put("3", 2)
p1 = obj.get("3")
p1 = obj.get("2")
obj.put("4", 3)
p1 = obj.get("2")
p2 = obj.get("3")
p2 = obj.get("4")

# ["LRUCache","put","put","get","get","put","get","get","get"]
# [[2],[2,1],[3,2],[3],[2],[4,3],[2],[3],[4]]

obj = LRUCache(2)
obj.put("1", 1) # [1]
obj.put("2", 2) # [1, 2]
p1 = obj.get("1") # [2, 1]
obj.put("3", 3) # [1, 3]
p2 = obj.get("2") # -1
pass