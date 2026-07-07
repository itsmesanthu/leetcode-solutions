class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i,j=1,max(piles)
        while i<=j:
            m=(i+j)//2
            hours=0
            for a in piles:
                hours+=(a+m-1)//m
            if hours<=h:
                j=m-1
            else:
                i=m+1
        return i