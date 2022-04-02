# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # find middle
        slow, fast = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # reverse list
        prev = None
        while slow: 
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        
        # check if are polindrome
        l, r = head, prev
        while r:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True
    
            
        
        
        
       
        