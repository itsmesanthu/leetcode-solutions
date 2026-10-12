class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def found(first):
            l,r=0,len(nums)-1
            res=-1
            while l<=r:
                m=(l+r)//2
                if nums[m]==target:
                    res=m
                    if first:
                        r=m-1
                    else:
                        l=m+1
                elif nums[m]<target:
                    l=m+1
                else:
                    r=m-1
            return res
        return [found(True),found(False)] 