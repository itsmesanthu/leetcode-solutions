class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dup=[]
        dict={}
        for i in nums:
            if i in dict:
                dict[i]+=1
                dup.append(i)
            else:
                dict[i]=1
        return dup