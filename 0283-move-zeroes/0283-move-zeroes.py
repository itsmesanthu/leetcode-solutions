class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        inn=0
        for i in range(n):
            if nums[i]!=0:
                nums[i],nums[inn]=nums[inn],nums[i]
                inn+=1
        return nums
