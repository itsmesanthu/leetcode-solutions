class Solution:
    def reverse(self, x: int) -> int:
        temp=x
        rev=0
        if x <0:
            x=x*-1
        while x>0:
            rem=x%10
            rev=(rev*10)+rem
            x=x//10
        if temp<0:
            rev= -rev
        if rev < -2**31 or rev > 2**31 - 1:
            return 0
        return rev