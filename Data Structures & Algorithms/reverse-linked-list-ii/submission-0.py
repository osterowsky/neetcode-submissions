# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        dummy = ListNode(next=head)
        before_left = dummy

        # Get left-most element
        for _ in range(left - 1):
            before_left = before_left.next

        # 'curr' is the first node of the sub-list to be reversed
        curr = before_left.next
        
        # Reverse the sub-list in place
        for _ in range(right - left):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = before_left.next
            before_left.next = next_node
            
        return dummy.next