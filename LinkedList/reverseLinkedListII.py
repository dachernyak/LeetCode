# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        curr = head
        prev = None
        dummy = ListNode(0, head)
        left_prev = dummy
      
   
        for i in range(left-1):
            left_prev = left_prev.next
            curr = curr.next
        # reverse
        for j in range(right-left+1):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
          
        # adding edges   
        left_prev.next.next = next_node
        left_prev.next = prev

        return dummy.next