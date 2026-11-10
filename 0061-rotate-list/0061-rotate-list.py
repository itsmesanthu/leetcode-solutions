# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode | None, k: int) -> ListNode | None:
        if not head or not head.next:
            return head
        t=head
        l=1
        while t.next:
            t=t.next
            l+=1
        k=k%l
        if k==0:
            return head
        t.next=head
        n=head
        for _ in range(l-k-1):
            n=n.next
        nh=n.next
        n.next=None
        return nh