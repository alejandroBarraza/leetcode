# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # find if there is a cycle
        slow, fast = head,head
        cycle = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                cycle = True
                break
        # if there is a cycle
        if cycle:
            s2 = head
            while s2 != slow:
                s2 = s2.next
                slow = slow.next
                
            return s2
        return None
            
        
        
            
        
                
        
            
        