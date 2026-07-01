# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i,j=0,n
        an=n
        while i<=j:
            m=(i+j)//2
            if isBadVersion(m):
                an=m
                j=m-1
            else:
                i=m+1
        return an