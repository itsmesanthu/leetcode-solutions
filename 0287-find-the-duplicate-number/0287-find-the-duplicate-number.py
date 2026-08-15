class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # d={}
        # for i in nums:
        #     if i not in d:
        #         d[i]=1
        #     else:
        #         d[i]+=1
        # for key,val in d.items():
        #     if val>1:
        #         return key
        visited=[False]*(len(nums))
        for i in nums:
            if visited[i]:
                return i
            visited[i]=True
        return 0
