from typing import List

class LinkedList:
    def __init__(self, key, val, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = LinkedList(-1, -1)
        self.tail = LinkedList(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.map = {}
        

    def get(self, key: int) -> int:
        # if key doesn't exist, return -1
        if key not in self.map:
            return -1

        # otherwise, return value and make MRU
        self.remove(self.map[key])
        self.insert(self.map[key])

        return self.map[key].val
        

    def put(self, key: int, value: int) -> None:
        # if already exists, make MRU
        if key in self.map:
            self.remove(self.map[key])

        # if not, create it as MRU
        new_node = LinkedList(key, value)
        self.insert(new_node)
        self.map[key] = new_node

        # if at capacity, remove LRU
        if len(self.map) > self.capacity:
            del self.map[self.head.next.key]
            self.remove(self.head.next)


    def insert(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
        

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        

obj = LRUCache(2)
obj.put("2", 1)
obj.put("3", 2)
p1 = obj.get("3")
p1 = obj.get("2")
obj.put("4", 3)
p1 = obj.get("2")
p2 = obj.get("3")
p2 = obj.get("4")