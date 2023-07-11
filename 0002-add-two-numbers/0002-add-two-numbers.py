class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2:
            sum_val = carry

            if l1:
                sum_val += l1.val
                l1 = l1.next

            if l2:
                sum_val += l2.val
                l2 = l2.next

            carry = sum_val // 10
            current.next = ListNode(sum_val % 10)
            current = current.next

        if carry:
            current.next = ListNode(carry)

        return dummy.next
        

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
# Helper function to convert a list to a linked list
def listToLinkedList(lst):
    dummy = ListNode(0)
    current = dummy
    for val in lst:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list
def linkedListToList(node):
    lst = []
    while node:
        lst.append(node.val)
        node = node.next
    return lst