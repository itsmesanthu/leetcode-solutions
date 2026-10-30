class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        y=(sum(bobSizes)-sum(aliceSizes))//2
        bobSizes.sort()
        for x in aliceSizes:
            t=x+y
            l,r=0,len(bobSizes)-1
            while l<=r:
                m=(l+r)//2
                if bobSizes[m]==t:
                    return [x,t]
                elif bobSizes[m]<t:
                    l=m+1
                else:
                    r=m-1