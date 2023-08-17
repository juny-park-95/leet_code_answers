# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverseLinkedList(node, k):
            prev = None
            curr = node
            while k > 0:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
                k -= 1
            return prev

        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        while length >= k:
            group_start = prev_group_end.next
            group_end = prev_group_end.next
            for i in range(k):
                group_end = group_end.next
            prev_group_end.next = reverseLinkedList(group_start, k)
            group_start.next = group_end
            prev_group_end = group_start
            length -= k

        return dummy.next
        