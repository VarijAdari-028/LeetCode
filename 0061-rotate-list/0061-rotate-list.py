# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def rotateRight(self, head: 'ListNode', k: int) -> 'ListNode':
        if not head or not head.next or k == 0:
            return head
        
        # find length and tail
        n = 1
        tail = head
        while tail.next:
            tail = tail.next
            n += 1
        
        k %= n
        if k == 0:
            return head
        
        # make it circular
        tail.next = head
        
        # find new tail: (n - k - 1) steps from head
        steps_to_new_tail = n - k - 1
        new_tail = head
        for _ in range(steps_to_new_tail):
            new_tail = new_tail.next
        
        new_head = new_tail.next
        new_tail.next = None
        
        return new_head