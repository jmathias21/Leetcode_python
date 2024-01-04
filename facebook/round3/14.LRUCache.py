from typing import List

class LinkedList:
    def __init__(self, val=-1, key=-1, next=None, prev=None):
        self.val = val
        self.key = key
        self.next = next
        self.prev= prev

# 
# Tags: 
# Time: started 2:24
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = LinkedList(-1, -1)
        self.tail = LinkedList(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}
        

    def get(self, key: int) -> int:
        if key not in self.map:
            return -1

        res = self.map[key]
        self.remove(res)
        self.add(res)
        return res.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.remove(self.map[key])

        node = LinkedList(value, key)
        self.add(node)
        self.map[key] = node

        if len(self.map) > self.capacity:
            del self.map[self.head.next.key]
            self.remove(self.head.next)


    def add(self, node):
        temp = self.tail.prev
        self.tail.prev = node
        node.next = self.tail
        node.prev = temp
        temp.next = node


    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

# ["LRUCache","get","put","get","put","put","get","get"]
# [[2],[2],[2,6],[1],[1,5],[1,2],[1],[2]]
# obj = LRUCache(2)
# p1 = obj.get(2) # -1
# obj.put(2,6) # [6]
# p1 = obj.get(1) # [6], -1
# obj.put(1,5) # [6,5]
# obj.put(1,2) # [6,2]
# p1 = obj.get(1) # [6,2], 2
# p1 = obj.get(2) # [6,2], 6


obj = LRUCache(2)
obj.put(1,1)
obj.put(2,2)
p1 = obj.get(1)
obj.put(3,3)
p1 = obj.get(2)
obj.put(4,4)
p1 = obj.get(1)
p1 = obj.get(3)
p1 = obj.get(4)


# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]

# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4