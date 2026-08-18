# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def merge_two(l1, l2):
            dummy = ListNode()
            cur = dummy

            while l1 and l2:
                if l1.val <= l2.val:
                    cur.next = l1
                    l1 = l1.next
                else:
                    cur.next = l2
                    l2 = l2.next
                cur = cur.next

            cur.next = l1 or l2 
            return dummy.next
        
        if not lists:
            return None
        
        while len(lists) >= 2:
            l1 = lists.pop()
            l2 = lists.pop()
            lists.append(merge_two(l1, l2))
        
        return lists[0]