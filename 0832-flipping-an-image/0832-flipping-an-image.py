class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        r=[row[::-1] for row in image[::]]
        for i in r:
            for j in range(len(i)):
                if i[j]==0:
                    i[j]=1
                else:
                    i[j]=0
        return r