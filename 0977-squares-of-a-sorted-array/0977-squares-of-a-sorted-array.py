class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # l=0
        # r=len(nums)-1
        # a=[0]*len(nums)
        # i=len(nums)-1
        # while l<=r:
        #     if abs(nums[l])>abs(nums[r]):
        #         a[i]=nums[l]**2
        #         l+=1
        #     else:
        #         a[i]=nums[r]**2
        #         r-=1
        #     i-=1
        # return a
        l=0
        r=len(nums)-1
        a=[0]*len(nums)
        i=len(a)-1
        while l<=r:
            ls=nums[l]*nums[l]
            rs=nums[r]*nums[r]
            if ls>rs:
                a[i]=ls
                l+=1
            else:
                a[i]=rs
                r-=1
            i-=1
        return a