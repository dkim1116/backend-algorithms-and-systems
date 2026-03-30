from __future__ import annotations

# Sorted Stream Merge
#
# You are given k linked lists, each already sorted in ascending order.
# Merge them into one sorted linked list and return its head.
#
# Input: lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
# Output: [1, 1, 2, 3, 4, 4, 5, 6]
# Input: lists = []
# Output: []

class ListNode:
    def __init__(self, val: int = 0, next: ListNode | None = None):
        self.val = val
        self.next = next

import heapq

class Solution:
    def solve(self, lists: list[ListNode | None]) -> ListNode | None:
        minHeap = []

        for i, node in enumerate(lists):
            if node is not None:
                heapq.heappush(minHeap, (node.val, i, node))

        dummyNode = ListNode(0)
        tail = dummyNode

        while minHeap:
            val, i, node = heapq.heappop(minHeap)

            tail.next = node
            tail = node

            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node))

        return dummyNode.next
