# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find middle
        slow, fast = head,head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverser linked list
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        # reorder linked list
        left_head , right_head = head, prev
        while left_head and right_head:
            templ = left_head.next
            tempr = right_head.next
            left_head.next = right_head
            right_head.next = templ
            left_head = templ
            right_head = tempr
        
            
            
            
            


        