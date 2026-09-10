# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        slow.next = None # no broken the linke

        prev = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        cur1 = head
        cur2 = prev

        while cur1 and cur2:
            tmp1 = cur1.next
            tmp2 = cur2.next

            cur1.next = cur2
            cur2.next = tmp1

            cur1 = tmp1
            cur2 = tmp2
            