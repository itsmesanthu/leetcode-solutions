class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        i=max(weights)
        j=sum(weights)
        while i<=j:
            m=i+(j-i)//2
            d=1
            c=0
            for a in weights:
                if c+a>m:
                    d+=1
                    c=a
                else:
                    c+=a
            if d<=days:
                j=m-1
            else:
                i=m+1
        return i