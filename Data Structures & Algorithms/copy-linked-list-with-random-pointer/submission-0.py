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
        if not head:
            return None

        node_map = {None: None}

        curr = head

        while curr: #first loop, create nodes
            node_map[curr] = Node(curr.val)
            curr = curr.next

        curr = head

        while curr: #second loop add pointers
            node = node_map[curr] 
            node.next = node_map[curr.next]
            node.random = node_map[curr.random]
            curr = curr.next


        return node_map[head]
        