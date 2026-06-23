class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        a=(n*(n+1))//2
        c=0
        for i in nums:
            c+=i
        return a-c

        
        