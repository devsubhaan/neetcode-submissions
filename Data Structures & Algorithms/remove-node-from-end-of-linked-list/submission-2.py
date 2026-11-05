# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1 and head.next is None:
            return None
            
        l = 0
        length = 0
        curr = head
        previous = None

        while curr:
            length +=1
            curr = curr.next

        if length - n == 0:
            return head.next

        curr = head

        while curr:
            if l == length - n:
                previous.next = curr.next
                break

            l +=1
            previous = curr
            curr = curr.next

        return head
