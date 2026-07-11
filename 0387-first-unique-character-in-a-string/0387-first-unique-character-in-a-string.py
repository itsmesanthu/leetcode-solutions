class Solution:
    def firstUniqChar(self, s: str) -> int:
        d={}
        n=len(s)
        for ch in s:
            if ch in d:
                d[ch]+=1
            else:
                d[ch]=1
        for ch in range(0,n) :
            if d[s[ch]]==1:
                return ch
        return -1