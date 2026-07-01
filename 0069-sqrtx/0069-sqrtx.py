class Solution:
    def mySqrt(self, x: int) -> int:
        i,j=0,x
        while i<=j:
            m=i+(j-i)//2
            s=m*m
            if s == x:
                return m
            elif s<x:
                i=m+1
            else:
                j=m-1
        return j