# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummy = ListNode(0,head)
        l = dummy
        r = head
        
        # update right pointer at nth pos
        while n > 0 and r:
            r = r.next
            n-=1
            
        # move until r reach null
        while r:
            r = r.next
            l = l.next
         
        # l reach one before number to skip
        l.next = l.next.next
        return dummy.next
    
            
        
        