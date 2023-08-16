# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
    
        dummy = ListNode(-1)  # Dummy node to handle the new head
        dummy.next = head
        prev = dummy

        while head and head.next:
            first_node = head
            second_node = head.next

            # Swap the nodes
            prev.next = second_node
            first_node.next = second_node.next
            second_node.next = first_node

            # Update pointers for the next iteration
            prev = first_node
            head = first_node.next

        return dummy.next  # Return the new head
        