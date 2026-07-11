# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head):
        p=None
        c=head
        while c is not None:
            newnode=c.next
            c.next=p
            p=c
            c=newnode
        return p

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is  None or head.next is None:
            return True
        s=head
        f=head
        while f and f.next:
            s=s.next
            f=f.next.next
        sc=self.reverse(s)
        fi=head
        while sc:
            if fi.val!=sc.val:
                return False
            fi=fi.next
            sc=sc.next
        return True