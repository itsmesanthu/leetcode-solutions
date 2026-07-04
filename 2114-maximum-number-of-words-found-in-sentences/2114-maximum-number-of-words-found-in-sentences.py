class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max1=0
        for i in sentences:
            word=1
            for j in i :
                if j==" ":
                    word+=1
            max1=max(max1,word)
        return max1
    

            

        