# Pattern:
#     Hashmap + doubly linked list

# Approach:
#    I use a doubly linked list to maintain usage order in O(1). 
#    The most recently used node is near the head, and the least recently used node is near the tail. 
#    On get, I move the node to the front. 
#    On put, I update or insert the node at the front, and if capacity is exceeded, I evict the node before the tail.
#    I also use a hashmap to map each key to its node, which allows O(1) lookup.

# Time & Space complexity:
#     Time complexity is O(1) as insertion, removal, lookup are all constant time
#     Space complexity is O(capacity)

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node(0, 0)
        self.tail = Node(0, 0)

        self.head.next = self.tail
        self.tail.prev = self.head

    def _insert(self, node: Node) -> None:
        node.prev = self.head
        node.next = self.head.next

        self.head.next.prev = node
        self.head.next = node

    def _remove(self, node: Node) -> None:
        prev = node.prev
        next = node.next

        prev.next = next
        next.prev = prev

    def put(self, key: int, val: int) -> None:
        if key in self.cache:
            oldNode = self.cache[key]
            self._remove(oldNode)
            del self.cache[key]

        newNode = Node(key, val)
        self._insert(newNode)
        self.cache[key] = newNode

        if len(self.cache) > self.capacity:
            lastNode = self.tail.prev
            self._remove(lastNode)
            del self.cache[lastNode.key]

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self._remove(node)
        self._insert(node)

        return node.val
