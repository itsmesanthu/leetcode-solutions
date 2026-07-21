class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prafix=[0]*(n)
        for i in range(0,n):
            prafix[i]=prafix[i-1]+nums[i]
        return prafix