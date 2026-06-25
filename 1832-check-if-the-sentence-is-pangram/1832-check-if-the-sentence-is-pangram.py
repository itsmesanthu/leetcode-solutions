class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        dict1={}
        n=len(sentence)
        if n<26:
            return False
        for i in range(0,n):
            if sentence[i] in dict1:
                dict1[sentence[i]]=dict1[sentence[i]]+1
            else:
                dict1[sentence[i]]=1
        return len(dict1)==26