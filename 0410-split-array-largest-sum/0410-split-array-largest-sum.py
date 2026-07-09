class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        i=max(nums)
        j=sum(nums)
        while i<=j:
            m=i+(j-i)//2
            p=1
            c=0
            for e in nums:
                if c+e>m:
                    p+=1
                    c=e
                else:
                    c+=e
            if p<=k:
                j=m-1
            else:
                i=m+1
        return i