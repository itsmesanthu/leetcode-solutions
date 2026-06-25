class Solution:
    def create(self,s):
        ac=[0]*26
        wo=""
        for i in range(0,len(s)):
            ac[ord(s[i])-97]+=1
        for i in range(0,len(ac)):
            if ac[i]>0:
                wo+=chr(i+97)
                wo+=chr(ac[i]+48)
        return wo
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict1=defaultdict(list)
        for i in range(0, len(strs)):
            wo=self.create(strs[i])
            dict1[wo].append(strs[i])
        res=[]
        for key,val in dict1.items():
            res.append(val)
        return res