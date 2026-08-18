# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """

        1 -> 2 -> 3 -> 4

        |   |
        """
        cur = head
        prev = None

        while cur:
            nxt_cur = cur.next
            cur.next = prev
            prev = cur
            cur = nxt_cur
        
        return prev
            
