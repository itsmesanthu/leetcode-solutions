class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        n=len(nums)
        for i in range(0,n):
            dif=target-nums[i]
            if dif in d:
                return (d[dif],i)
            else:
                d[nums[i]]=i
        