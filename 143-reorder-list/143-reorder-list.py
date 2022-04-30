# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # loop over and find the middle of the linked list
        s, f = head,head
        
        while f and f.next:
            s = s.next
            f = f.next.next
            
        # after, slow is in the middle of the linked list and breake it
        secondList = s.next
        s.next = None
        
        # reverse the list from slow
        prev = None
        while secondList:
            currNext = secondList.next
            secondList.next = prev
            prev = secondList
            secondList = currNext
        newSecondHead = prev
            
        # i already break the linked ist
        while head and newSecondHead:
            tmpHead = head.next
            tmpSecondHead = newSecondHead.next
            head.next = newSecondHead
            newSecondHead.next = tmpHead
            head = tmpHead
            newSecondHead = tmpSecondHead
        
            