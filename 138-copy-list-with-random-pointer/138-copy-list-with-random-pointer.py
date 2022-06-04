"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # creata a copy of new node in a hp
        # "oldNode" : "newNode"
        curr = head
        oldToCopy = { None: None}
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
            
        # Connect the links in the new copy
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy[curr.next]
            copy.random = oldToCopy[curr.random]
            curr = curr.next
        return oldToCopy[head]
        
        
            
            
            
            # {
            #     "[7:13:None]": [7:None,None]
            #      "[13,11,7]" : [13.[13,11,7],None]
            #       "[11,10,1]" : [13.None,None]
            # }
            
            
            
            
            
            
        