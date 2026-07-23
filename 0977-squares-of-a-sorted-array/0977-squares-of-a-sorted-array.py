class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l=0
        r=len(nums)-1
        a=[0]*len(nums)
        i=len(nums)-1
        while l<=r:
            if abs(nums[l])>abs(nums[r]):
                a[i]=nums[l]**2
                l+=1
            else:
                a[i]=nums[r]**2
                r-=1
            i-=1
        return a