class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        i=-1
        for j in range(0,n):
            if nums[j]!=val:
                i+=1
                nums[i],nums[j]=nums[j],nums[i]
        return i+1