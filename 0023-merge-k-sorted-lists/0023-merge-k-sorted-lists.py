# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = ListNode()
        curr = dummy
        counter = 0  # To handle multiple nodes with the same value

        # Add the first nodes of all linked lists to the min-heap
        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, counter, head))
                counter += 1

        while heap:
            # Extract the smallest node from the min-heap
            _, _, node = heapq.heappop(heap)

            # Add the node to the merged list
            curr.next = node
            curr = curr.next

            # Move the pointer of the linked list from which the node was extracted
            if node.next:
                heapq.heappush(heap, (node.next.val, counter, node.next))
                counter += 1

        return dummy.next