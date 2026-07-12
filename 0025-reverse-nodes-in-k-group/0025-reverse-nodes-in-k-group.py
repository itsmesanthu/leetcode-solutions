# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        current=head
        count=0
        while  current and count<k:
            current=current.next
            count+=1
        if count<k:
            return head
        prev=None
        current=head
        for _ in range(k):
            nxt=current.next
            current.next=prev
            prev=current
            current=nxt
        head.next=self.reverseKGroup(current,k)
        return prev