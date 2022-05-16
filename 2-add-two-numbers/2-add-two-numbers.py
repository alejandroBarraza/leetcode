# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy 
        2--- 4 ---8
        2----3 ---8
        curry = 0
        while l1 or l2 or curry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            val = val1 + val2 + curry
            
            #example if nuber is 16
            curry = val // 10
            val = val % 10
            
            # insert in the linkedlist
            curr.next = ListNode(val)
            
            # update pointers
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            
        return dummy.next
            
            
            
            
            
                
        
        