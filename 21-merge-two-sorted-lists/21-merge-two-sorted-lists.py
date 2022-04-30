# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        tail = dummy
        
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                # list2 >= list1
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # check if a list ended
        if list1 is None:
            tail.next = list2
        
        if list2 is None:
            tail.next = list1
            
        # return the new head of the new linked list
        return dummy.next
        
        
        
        
            
            
        