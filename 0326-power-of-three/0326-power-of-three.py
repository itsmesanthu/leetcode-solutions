class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # method one to solve this time complesity is o(log3 n)
        # if n<=0:
        #     return False
        # while n%3==0:
        #     n//=3
        # return n==1
        return n>0 and (3**19)%n==0
        