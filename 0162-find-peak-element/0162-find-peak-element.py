class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        i,j=0,len(nums)-1
        while i<j:
            m=(i+j)//2
            if nums[m]<nums[m+1]:
                i=m+1
            else:
                j=m
        return i
            
