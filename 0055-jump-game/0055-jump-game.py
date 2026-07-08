class Solution:
    def canJump(self, nums: List[int]) -> bool:
        ma=0
        for i in range(0,len(nums)):
            if i>ma:
                return False
            ma=max(i+nums[i],ma)
        return True