class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1={}
        if len(s)!=len(t):
            return False
        else:
            for i in s:
                if i in dict1:
                    dict1[i]+=1
                else:
                    dict1[i]=1
            for i in t:
                if i in dict1:
                    dict1[i]-=1
                else:
                    dict1[i]=-1
            for i in dict1:
                if dict1[i]!=0:
                    return False
            return True