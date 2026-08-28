class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = first.next

            # rewire: prev -> second -> first -> (rest)
            first.next = second.next
            second.next = first
            prev.next = second

            prev = first

        return dummy.next