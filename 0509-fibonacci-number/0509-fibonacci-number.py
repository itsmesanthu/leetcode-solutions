class Solution:
    def fib(self, n: int) -> int:
        n1,n2=0,1
        while n>0:
            temp=n1+n2
            n1=n2
            n2=temp
            n-=1
        return n1