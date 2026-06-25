class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        s,e=0,len(arr)-1
        while s<e:
            m=(s+e)//2
            if  arr[m]<arr[m+1]:
                s=m+1
            else:
                e=m
        return s