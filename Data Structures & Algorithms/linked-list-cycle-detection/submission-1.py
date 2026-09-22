# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hm = {}

        curr = head
        while curr and curr.next:
            if not curr in hm:
                hm[curr] = 1
            else:
                return True
            curr = curr.next
        
        return False