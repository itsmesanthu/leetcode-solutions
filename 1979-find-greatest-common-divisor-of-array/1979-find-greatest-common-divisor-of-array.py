class Solution:
    def findGCD(self, nums: list[int]) -> int:
        s=min(nums)
        l=max(nums)
        gcd=0
        for i in range(1,s+1):
            if s%i==0 and l%i==0:
                gcd=i
        return gcd