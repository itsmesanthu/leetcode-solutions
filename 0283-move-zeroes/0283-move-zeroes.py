class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i=-1
        for j in range(0,n):
            if nums[j]!=0:
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
        return nums
