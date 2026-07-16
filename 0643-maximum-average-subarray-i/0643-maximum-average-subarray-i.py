class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        s=sum(nums[:k])
        n=len(nums)
        m=s
        for i in range(k,n):
            s+=nums[i]
            s-=nums[i-k]
            m=max(m,s)
        return m/k