# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # check if there are at least k nodes left from `node`
        def has_k_nodes(node, k):
            count = 0
            while node and count < k:
                node = node.next
                count += 1
            return count == k

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            if not has_k_nodes(group_prev.next, k):
                break

            prev, curr = None, group_prev.next
            group_tail = curr  # will become the tail of this group after reversal

            for _ in range(k):
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            # prev is now the new head of this reversed group
            group_prev.next = prev
            group_tail.next = curr
            group_prev = group_tail

        return dummy.next