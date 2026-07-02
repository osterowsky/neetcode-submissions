# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a: int, b: int) -> int:
            while b != 0:
                a, b = b, a % b
            return a
            
        if not head.next:
            return head
        
        prev, cur = head, head.next
        while cur:
            val = gcd(max(prev.val, cur.val), min(prev.val, cur.val))
            prev.next = ListNode(val=val, next=cur)
            prev = cur
            cur = cur.next
        
        return head