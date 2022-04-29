# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        # find the length and tail
        length, tail  = 1, head
        while tail and tail.next:
            tail = tail.next
            length+=1
        
        k = k % length
        if k == 0:
            return head
        
        # move until k and break the link
        current = head
        for i in range(length - k - 1):
            current = current.next
        # when i reach k , current.next will be the new head.
        newHead = current.next
        
        # destroy the link from the current node
        current.next = None
        
        # now join the tail to the old head(first element)
        tail.next = head
        return newHead
        
        
        
        
        