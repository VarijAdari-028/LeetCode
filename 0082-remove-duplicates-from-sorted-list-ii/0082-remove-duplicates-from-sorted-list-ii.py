# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        while curr:
            if curr.next and curr.val == curr.next.val:
                dup = curr.val
                while curr and curr.val == dup:   # skip the whole run
                    curr = curr.next
                prev.next = curr                  # unlink all copies
            else:
                prev = curr                       # curr is unique, keep it
                curr = curr.next

        return dummy.next