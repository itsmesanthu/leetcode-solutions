class Solution:
    def maxProduct(self, n: int) -> int:
        m1,m2=0,0
        while n>0:
            d=n%10
            n//=10
            if d>m1:
                m2=m1
                m1=d
            elif d>m2:
                m2=d
        return m1*m2