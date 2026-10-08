class Solution:
    def fib(self, n: int) -> int:
        # if n<=1:
        #     return n
        # a,b=0,1
        # for _ in range(2,n+1):
        #     a,b=b,a+b
        # return b
        n1,n2=0,1
        while n>0:
            temp=n1+n2
            n1=n2
            n2=temp
            n-=1
        return n1