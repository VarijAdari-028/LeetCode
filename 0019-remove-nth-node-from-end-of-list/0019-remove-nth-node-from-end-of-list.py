class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        left = dummy
        right = dummy

        # Move right n+1 steps ahead
        for _ in range(n + 1):
            right = right.next

        # Move both until right reaches the end
        while right:
            left = left.next
            right = right.next

        # Remove the nth node from the end
        left.next = left.next.next

        return dummy.next