# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        prev = None
        max_sum = 0


        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        while slow:

            nxt_node = slow.next
            slow.next = prev
            prev = slow
            slow = nxt_node
        
        while prev:
            max_sum = max(max_sum, prev.val + head.val)
            prev = prev.next
            head = head.next
  
        return max_sum