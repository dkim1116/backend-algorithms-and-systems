# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

# Pattern:
#     minHeap merge

# Approach:
#     I use a minHeap to store the current head node from each linked list.
#     I construct a dummyHead as tail of a LinkedList then append the ListNodes in order
#     Each time I pop the smallest node from the heap, I append it to the merged list.
#     If the popped ListNode has next then I add that to the heap

# Time & Space complexity:
#     Time complexity is O(n log k) where n is the size of ListNodes and k is the number of lists
#     Space complexity is O(k) where k represents the size of the heap


import heapq

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: list[ListNode]) -> ListNode:
        minHeap = []

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(minHeap, (node.val, i, node))

        dummyNode = ListNode(0)
        tail = dummyNode

        while minHeap:
            val, i, node = heapq.heappop(minHeap)

            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))

        return dummyNode.next