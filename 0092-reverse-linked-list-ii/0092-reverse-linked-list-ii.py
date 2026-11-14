# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next             # node just before position left

        curr = prev.next                 # first node of the sublist (ends up last)
        for _ in range(right - left):
            nxt = curr.next              # node to move to the front
            curr.next = nxt.next         # unlink it
            nxt.next = prev.next         # point it at the current front
            prev.next = nxt              # make it the new front

        return dummy.next