# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        """
        listLength = 0
        while curr != None:
            listLength +=1
            curr = curr.next
        """
        # Split the list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
 
        l2 = slow.next
        slow.next = None

        # Reverse second half
        previous = None
        while l2 != None:
            nextNode = l2.next
            l2.next = previous
            previous = l2
            l2 = nextNode


        l1 = head
        l2 = previous
        
        while l2:
            tmp1 = l1.next
            tmp2 = l2.next
            l1.next = l2
            l2.next = tmp1

            l1 = tmp1
            l2 = tmp2










            