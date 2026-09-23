class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # res=[]
        # for i in range(min(len(word1),len(word2))):
        #     res.append(word1[i])
        #     res.append(word2[i])
        # res.append(word1[len(word2):])
        # res.append(word2[len(word1):])
        # return "".join(res)
        res=""
        l=min(len(word1),len(word2))
        for i in range(l):
            res+=word1[i]+word2[i]
        res+=(word1[l:] if len(word1)>len(word2) else word2[l:])
        return res