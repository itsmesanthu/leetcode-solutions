class Solution:
    def findMin(self, nums: List[int]) -> int:
        # a=nums[0]
        # for i in range(1,len(nums)-1):
        #     a=min(a,nums[i])
        # return a
        i,j=0,len(nums)-1
        while i<j:
            m=(i+j)//2
            if nums[m]>nums[j]:
                i=m+1
            else:
                j=m
        return nums[i]
            
