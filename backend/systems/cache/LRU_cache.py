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
