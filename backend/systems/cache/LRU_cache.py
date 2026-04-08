# Design a data structure that follows the Least Recently Used (LRU) cache policy.
#
# Implement the `LRUCache` class:
# - `LRUCache(capacity: int)` initializes the cache with a positive capacity.
# - `get(key: int) -> int` returns the value of the key if it exists, otherwise returns -1.
# - `put(key: int, value: int) -> None` inserts or updates the key with the given value.
#
# If inserting a new key causes the cache to exceed capacity, evict the least recently used key.
# A key becomes most recently used whenever it is accessed by `get` or updated/inserted by `put`.
#
# Both `get` and `put` should run in average O(1) time.
#
# Example:
# cache = LRUCache(2)
# cache.put(1, 1)         # cache is {1=1}
# cache.put(2, 2)         # cache is {1=1, 2=2}
# cache.get(1)            # returns 1
# cache.put(3, 3)         # evicts key 2, cache is {1=1, 3=3}
# cache.get(2)            # returns -1
# cache.put(4, 4)         # evicts key 1, cache is {4=4, 3=3}
# cache.get(1)            # returns -1
# cache.get(3)            # returns 3
# cache.get(4)            # returns 4
#
# Constraints:
# - 1 <= capacity <= 3000
# - 0 <= key <= 10^4
# - 0 <= value <= 10^5
# - At most 2 * 10^5 calls will be made to `get` and `put`.

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}

        self.head = Node(0, 0)  # dummy head
        self.tail = Node(0, 0)  # dummy tail

        self.head.next = self.tail
        self.tail.prev = self.head

# Insert
# with a node, add to the head of the linkedList
# adjust dummy head to point to the new head 
# and the next node of head to point at new node
    def _insert(self, node: Node) -> None:
        node.next = self.head.next
        node.prev = self.head

        self.head.next.prev = node
        self.head.next = node

# Remove
# remove the last node from tail
    def _remove(self, node: Node) -> None:
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key not in self.hashmap:
            return -1

        node = self.hashmap[key]
        self._remove(node)
        self._insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            old_node = self.hashmap[key]
            self._remove(old_node)

        new_node = Node(key, value)
        self.hashmap[key] = new_node
        self._insert(new_node)

        if len(self.hashmap) > self.capacity:
            lru_node = self.tail.prev
            self._remove(lru_node)
            del self.hashmap[lru_node.key]

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)