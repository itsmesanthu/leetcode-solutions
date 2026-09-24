# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        p=None
        c=head
        while c is not None:
            n=c.next
            c.next=p
            p=c
            c=n
        return p