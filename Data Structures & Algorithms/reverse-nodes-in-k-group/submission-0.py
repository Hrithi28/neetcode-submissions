# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Check if there are at least k nodes
        curr = head
        count = 0
        while curr and count < k:
            curr = curr.next
            count += 1

        # If fewer than k nodes, return as it is
        if count < k:
            return head

        # Reverse first k nodes
        prev = None
        curr = head
        for _ in range(k):
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Connect with remaining list
        head.next = self.reverseKGroup(curr, k)

        return prev